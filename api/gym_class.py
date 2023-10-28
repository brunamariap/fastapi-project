from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import SessionFactory
from domain.request.members import GymClassReq
from domain.data.sqlalchemy_models import Gym_Class
from repository.sqlalchemy.members import GymClassRepository
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


@router.post("/gym_class/add")
async def add_gym_class(req: GymClassReq, sess: Session = Depends(sess_db)):
    pass


@router.get("/gym_class/list")
async def list_gym_class(sess: Session = Depends(sess_db)):
    pass


@router.patch("/gym_class/update")
def update_gym_class(id: int, req: GymClassReq, sess: Session = Depends(sess_db)):
    pass


@router.delete("/gym_class/delete/{id}")
def delete_gym_class(id: int, sess: Session = Depends(sess_db)):
    pass


@router.get("/gym_class/list/{id}", response_model=GymClassReq)
def get_gym_class(id: int, sess: Session = Depends(sess_db)):
    pass