from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import SessionFactory
from domain.request.signup import SignupReq
from domain.data.sqlalchemy_models import Signup
from repository.sqlalchemy.signup import LoginMemberRepository, MemberAttendanceRepository
from typing import List

from cqrs.admin.command.create_handlers import AddSignupCommandHandler
from cqrs.admin.command.update_handlers import UpdateSignupCommandHandler
from cqrs.admin.command.delete_handlers import DeleteSignupCommandHandler
from cqrs.admin.query.query_handlers import SignupQueryHandler, GetSignupQuery
from cqrs.queries import SignupListQuery
from cqrs.commands import SignupCommand


router = APIRouter()


def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()


@router.post("/signup/add")
def add_signup(req: SignupReq, sess: Session = Depends(sess_db)):
    handler = AddSignupCommandHandler(sess)
    signup = Signup(password=req.password, username=req.username, id=req.id)
    command = SignupCommand()
    command.details = signup
    result = handler.handle(command)

    if result == True:
        return req
    else:
        return JSONResponse(content={'message': 'create signup problem encountered'}, status_code=500)


@router.get("/signup/list", response_model=List[SignupReq])
def list_signup(sess: Session = Depends(sess_db)):
    handler = SignupQueryHandler(sess)
    query: SignupListQuery = handler.handle()
    return query.records


@router.patch("/signup/update")
def update_signup(id: int, req: SignupReq, sess: Session = Depends(sess_db)):
    signup_dict = req.dict(exclude_unset=True)
    handler = UpdateSignupCommandHandler(sess)
    command = SignupCommand()
    command.details = signup_dict
    result = handler.handle(id, command)
    if result:
        return JSONResponse(content={'message': 'profile updated successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'update profile error'}, status_code=500)


@router.delete("/signup/delete/{id}")
def delete_signup(id: int, sess: Session = Depends(sess_db)):
    handler = DeleteSignupCommandHandler(sess)
    result = handler.handle(id)
    
    if result:
        return JSONResponse(content={'message': 'profile deleted successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'delete profile error'}, status_code=500)


@router.get("/signup/list/{id}", response_model=SignupReq)
def get_signup(id: int, sess: Session = Depends(sess_db)):
    handler = GetSignupQuery(sess, id)
    query: SignupListQuery = handler.handle()
    return query.records


@router.get("/login/memberslist")
def get_join_login_members(sess: Session = Depends(sess_db)):
    repo: LoginMemberRepository = LoginMemberRepository(sess)
    result = repo.join_login_members()
    return result


@router.get("/member/attendance")
def get_join_member_attendance(sess: Session = Depends(sess_db)):
    repo: MemberAttendanceRepository = MemberAttendanceRepository(sess)
    result = repo.join_member_attendance()
    return result
