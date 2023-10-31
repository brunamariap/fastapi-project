from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import SessionFactory
from domain.request.members import ProfileMembersReq, GymClassReq
from domain.data.sqlalchemy_models import Profile_Members

from cqrs.members.command.create_handlers import AddMemberCommandHandler
from cqrs.members.command.update_handlers import UpdateMemberCommandHandler
from cqrs.members.command.delete_handlers import DeleteMemberCommandHandler
from cqrs.commands import ProfileMemberCommand
from cqrs.members.query.query_handlers import ListMembersQueryHandler, GetMemberQueryHandler
from cqrs.queries import ProfileMemberListQuery

router = APIRouter()

def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()


@router.post("/members/add")
async def add_member(req: ProfileMembersReq, sess: Session = Depends(sess_db)):
    handler = AddMemberCommandHandler()
    member = Profile_Members(firstname=req.firstname, lastname=req.lastname, age=req.age, height=req.height, weight=req.weight, membership_type=req.membership_type, trainer_id=req.trainer_id, id=req.id)
    command = ProfileMemberCommand()
    command.details = member
    result = handler.handle(command)

    if result == True:
        return req
    else:
        return JSONResponse(content={"messgage": "create member problem encountere"}, status_code=500)


@router.get("/members/list")
async def list_members(sess: Session = Depends(sess_db)):
    handler = ListMembersQueryHandler(sess)
    query: ProfileMemberListQuery = handler.handle()
    return query.records


@router.patch("/members/update")
def update_member(id: int, req: ProfileMembersReq, sess: Session = Depends(sess_db)):
    member_dict = req.dict(exclude_unset=True)
    handler = UpdateMemberCommandHandler(sess)
    command = ProfileMemberCommand()
    command.details = member_dict
    result = handler.handle(id, command)

    if result:
        return JSONResponse(content={'message': 'member updated successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'update member error'}, status_code=500)


@router.delete("/members/delete/{id}")
def delete_member(id: int, sess: Session = Depends(sess_db)):
    handler = DeleteMemberCommandHandler(sess)
    result = handler.handle(id)
    if result:
        return JSONResponse(content={'message': 'member deleted successfully'}, status_code=200)
    else:
        return JSONResponse(content={'message': 'delete member error'}, status_code=500)


@router.get("/members/list/{id}", response_model=ProfileMembersReq)
def get_member(id: int, sess: Session = Depends(sess_db)):
    handler = GetMemberQueryHandler(sess, id)
    query: ProfileMemberListQuery = handler.handle()
    return query.records