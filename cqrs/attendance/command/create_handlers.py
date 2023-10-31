from repository.sqlalchemy.attendance import AttendanceRepository
from cqrs.commands import AttendanceMemberCommand
from cqrs.handlers import ICommandHandler

from sqlalchemy.orm import Session


class AddAttendanceCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: AttendanceRepository = AttendanceRepository(sess)
    def handle(self, command: AttendanceMemberCommand) -> bool:
        result = self.repo.insert_member(command.details)
        return result