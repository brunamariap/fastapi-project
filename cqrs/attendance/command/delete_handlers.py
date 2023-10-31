from repository.sqlalchemy.attendance import AttendanceRepository
from cqrs.handlers import ICommandHandler

from sqlalchemy.orm import Session


class DeleteAttendanceCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: AttendanceRepository = AttendanceRepository(sess)
    def handle(self, id:int) -> bool:
        result = self.repo.delete_member(id)
        return result