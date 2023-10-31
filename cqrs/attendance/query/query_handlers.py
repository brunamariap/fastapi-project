from repository.sqlalchemy.attendance import AttendanceRepository
from cqrs.queries import AttendanceListQuery
from cqrs.handlers import IQueryHandler

from sqlalchemy.orm import Session


class ListAttendanceQueryHandler(IQueryHandler):
    def __init__(self, sess: Session):
        self.repo: AttendanceRepository = AttendanceRepository(sess)
        self.query: AttendanceListQuery = AttendanceListQuery()
    def handle(self) -> AttendanceListQuery:
        data = self.repo.get_all_trainers()
        self.query.records = data
        return self.query
    

class GetAttendanceQueryHandler(IQueryHandler):
    def __init__(self, sess: Session, id: int):
        self.repo: AttendanceRepository = AttendanceRepository(sess)
        self.query: AttendanceListQuery = AttendanceListQuery()
        self.id = id
    def handle(self) -> AttendanceListQuery:
        data = self.repo.get_trainer(self.id)
        self.query.records = data
        return self.query