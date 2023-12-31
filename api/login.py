from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import SessionFactory
from domain.request.login import LoginReq
from domain.data.sqlalchemy_models import Login
from repository.sqlalchemy.login import LoginRepository
from typing import List

from cqrs.login.command.create_handlers import AddLoginCommandHandler
from cqrs.login.command.update_handlers import UpdateLoginCommandHandler
from cqrs.login.command.delete_handlers import DeleteLoginCommandHandler
from cqrs.commands import LoginCommand
from cqrs.login.query.query_handlers import ListLoginQueryHandler, GetLoginQueryHandler
from cqrs.queries import LoginListQuery


router = APIRouter()


def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()


@router.post("/login/add")
async def add_login(req: LoginReq, sess: Session = Depends(sess_db)):
    handler = AddLoginCommandHandler(sess)
    login = Login(id=req.id, username=req.username, password=req.password, date_approved=req.date_approved, user_type=req.user_type)

    command = LoginCommand()
    command.details = login
    result = handler.handle(command)
    
    if result == True:
        return login
    else:
        return JSONResponse(content={'message': 'create login problem encountered'}, status_code=500)


@router.patch("/login/update")
async def update_login(id: int, req: LoginReq, sess: Session = Depends(sess_db)):
    login_dict = req.dict(exclude_unset=True)
    handler = UpdateLoginCommandHandler(sess)
    command = LoginCommand()
    command.details = login_dict
    result = handler.handle(id, command)
    if result:
        return JSONResponse(content={'message': 'login updated successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'update login error'}, status_code=500)


@router.delete("/login/delete/{id}")
async def delete_login(id: int, sess: Session = Depends(sess_db)):
    handler = DeleteLoginCommandHandler(sess)
    result = handler.handle(id)
    if result:
        return JSONResponse(content={'message': 'login deleted successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'delete login error'}, status_code=500)


@router.get("/login/list")
async def list_login(sess: Session = Depends(sess_db)):
    handler = ListLoginQueryHandler(sess)
    query: LoginListQuery = handler.handle()
    return query.records


@router.get("/login/get/{id}")
async def get_login(id: int, sess: Session = Depends(sess_db)):
    handler = GetLoginQueryHandler(sess, id)
    query: LoginListQuery = handler.handle()
    return query.records
