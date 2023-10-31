from repository.sqlalchemy.members import MembersRepository, GymClassRepository
from cqrs.commands import ProfileMemberCommand, GymClassCommand
from cqrs.handlers import ICommandHandler

from sqlalchemy.orm import Session


class UpdateMemberCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: MembersRepository = MembersRepository(sess)
    def handle(self, id:int, command: ProfileMemberCommand) -> bool:
        result = self.repo.update_member(id, command.details)
        return result


class UpdateGymClassCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: GymClassRepository = GymClassRepository(sess)
    def handle(self, id:int, command: GymClassCommand) -> bool:
        result = self.repo.update_gym_class(id, command.details)
        return result