from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import SessionFactory
from domain.request.attendance import AttendanceMemberReq
from domain.data.sqlalchemy_models import Attendance_Member

from cqrs.attendance.command.create_handlers import AddAttendanceCommandHandler
from cqrs.attendance.command.update_handlers import UpdateAttendanceCommandHandler
from cqrs.attendance.command.delete_handlers import DeleteAttendanceCommandHandler
from cqrs.commands import AttendanceMemberCommand
from cqrs.attendance.query.query_handlers import ListAttendanceQueryHandler, GetAttendanceQueryHandler
from cqrs.queries import AttendanceListQuery

router = APIRouter()

def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()


@router.post("/attendance/add")
async def add_attendance(req: AttendanceMemberReq, sess: Session = Depends(sess_db)):
    handler = AddAttendanceCommandHandler(sess)
    member = Attendance_Member(member_id=req.member_id, timeout=req.timeout, timein=req.timein, date_log=req.date_log, id=req.id)
    command = AttendanceMemberCommand()
    command.details = member
    result = handler.handle(command)

    if result == True:
        return req
    else:
        return JSONResponse(content={"messgage": "create attendance member problem encountere"}, status_code=500)



@router.get("/attendance/list")
async def list_attendance(sess: Session = Depends(sess_db)):
    handler = ListAttendanceQueryHandler(sess)
    query: AttendanceListQuery = handler.handle()
    return query.records


@router.patch("/attendance/update")
def update_attendance(id: int, req: AttendanceMemberReq, sess: Session = Depends(sess_db)):
    member_dict = req.dict(exclude_unset=True)
    handler = UpdateAttendanceCommandHandler(sess)
    command = AttendanceMemberCommand()
    command.details = member_dict
    result = handler.handle(id, command)

    if result:
        return JSONResponse(content={'message': 'member updated successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'update member error'}, status_code=500)


@router.delete("/attendance/delete/{id}")
def delete_attendance(id: int, sess: Session = Depends(sess_db)):
    handler = DeleteAttendanceCommandHandler(sess)
    result = handler.handle(id)
    if result:
        return JSONResponse(content={'message': 'member deleted successfully'}, status_code=200)
    else:
        return JSONResponse(content={'message': 'delete member error'}, status_code=500)


@router.get("/attendance/list/{id}", response_model=AttendanceMemberReq)
def get_attendance(id: int, sess: Session = Depends(sess_db)):
    handler = GetAttendanceQueryHandler(sess, id)
    query: AttendanceListQuery = handler.handle()
    return query.records