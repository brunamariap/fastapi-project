from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import SessionFactory
from domain.request.members import ProfileMembersReq, GymClassReq
from domain.data.sqlalchemy_models import Profile_Members
from repository.sqlalchemy.members import MembersRepository
from typing import List

from cqrs.trainers.command.create_handlers import AddTrainerCommandHandler
from cqrs.commands import ProfileTrainerCommand
from cqrs.trainers.query.query_handlers import ListTrainerQueryHandler, ProfileTrainerListQuery

router = APIRouter()

def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()


@router.post("/members/add")
async def add_member(req: ProfileMembersReq, sess: Session = Depends(sess_db)):
    pass


@router.get("/members/list")
async def list_members(sess: Session = Depends(sess_db)):
    pass


@router.patch("/members/update")
def update_member(id: int, req: ProfileMembersReq, sess: Session = Depends(sess_db)):
    pass


@router.delete("/members/delete/{id}")
def delete_member(id: int, sess: Session = Depends(sess_db)):
    pass


@router.get("/members/list/{id}", response_model=ProfileMembersReq)
def get_member(id: int, sess: Session = Depends(sess_db)):
    pass