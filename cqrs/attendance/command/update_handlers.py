from repository.sqlalchemy.attendance import AttendanceRepository
from cqrs.commands import AttendanceMemberCommand
from cqrs.handlers import ICommandHandler

from sqlalchemy.orm import Session


class UpdateAttendanceCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: AttendanceRepository = AttendanceRepository(sess)
    def handle(self, id:int, command: AttendanceMemberCommand) -> bool:
        result = self.repo.update_member(id, command.details)
        return result