from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import SessionFactory
from domain.request.attendance import AttendanceMemberReq
from domain.data.sqlalchemy_models import Attendance_Member
from repository.sqlalchemy.attendance import AttendanceRepository
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


@router.post("/attendance/add")
async def add_attendance(req: AttendanceMemberReq, sess: Session = Depends(sess_db)):
    pass


@router.get("/attendance/list")
async def list_attendance(sess: Session = Depends(sess_db)):
    pass


@router.patch("/attendance/update")
def update_attendance(id: int, req: AttendanceMemberReq, sess: Session = Depends(sess_db)):
    pass


@router.delete("/attendance/delete/{id}")
def delete_attendance(id: int, sess: Session = Depends(sess_db)):
    pass


@router.get("/attendance/list/{id}", response_model=AttendanceMemberReq)
def get_attendance(id: int, sess: Session = Depends(sess_db)):
    pass