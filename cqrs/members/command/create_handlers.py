from repository.sqlalchemy.members import MembersRepository, GymClassRepository
from cqrs.commands import ProfileMemberCommand
from cqrs.handlers import ICommandHandler

from sqlalchemy.orm import Session


class AddMemberCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: MembersRepository = MembersRepository(sess)
    def handle(self, command: ProfileMemberCommand) -> bool:
        result = self.repo.insert_member(command.details)
        return result
    

class AddGymClassCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: GymClassRepository = GymClassRepository(sess)
    def handle(self, command: ProfileMemberCommand) -> bool:
        result = self.repo.insert_gym_class(command.details)
        return result
