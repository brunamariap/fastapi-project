from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import SessionFactory
from domain.request.members import GymClassReq
from domain.data.sqlalchemy_models import Gym_Class
from repository.sqlalchemy.members import GymClassRepository
from typing import List

from cqrs.members.command.create_handlers import AddGymClassCommandHandler
from cqrs.members.command.update_handlers import UpdateGymClassCommandHandler
from cqrs.members.command.delete_handlers import DeleteGymClassCommandHandler
from cqrs.commands import GymClassCommand
from cqrs.members.query.query_handlers import ListGymClassQueryHandler, GetGymClassQueryHandler
from cqrs.queries import GymClassListQuery

router = APIRouter()

def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()


@router.post("/gym_class/add")
async def add_gym_class(req: GymClassReq, sess: Session = Depends(sess_db)):
    handler = AddGymClassCommandHandler(sess)
    gym_class = Gym_Class(name=req.name, member_id=req.member_id, trainer_id=req.trainer_id, aprroved_id=req.approved, id=req.id)
    command = GymClassCommand()
    command.details = gym_class
    result = handler.handle(command)

    if result == True:
        return req
    else:
        return JSONResponse(content={"messgage": "create member problem encountere"}, status_code=500)


@router.get("/gym_class/list")
async def list_gym_class(sess: Session = Depends(sess_db)):
    handler = ListGymClassQueryHandler(sess)
    query: GymClassListQuery = handler.handle()
    return query.records


@router.patch("/gym_class/update")
def update_gym_class(id: int, req: GymClassReq, sess: Session = Depends(sess_db)):
    member_dict = req.dict(exclude_unset=True)
    handler = UpdateGymClassCommandHandler(sess)
    command = GymClassCommand()
    command.details = member_dict
    result = handler.handle(id, command)

    if result:
        return JSONResponse(content={'message': 'member updated successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'update member error'}, status_code=500)


@router.delete("/gym_class/delete/{id}")
def delete_gym_class(id: int, sess: Session = Depends(sess_db)):
    handler = DeleteGymClassCommandHandler(sess)
    result = handler.handle(id)
    if result:
        return JSONResponse(content={'message': 'member deleted successfully'}, status_code=200)
    else:
        return JSONResponse(content={'message': 'delete member error'}, status_code=500)


@router.get("/gym_class/list/{id}", response_model=GymClassReq)
def get_gym_class(id: int, sess: Session = Depends(sess_db)):
    handler = GetGymClassQueryHandler(sess, id)
    query: GymClassListQuery = handler.handle()
    return query.records