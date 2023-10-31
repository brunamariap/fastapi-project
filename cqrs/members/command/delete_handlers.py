from repository.sqlalchemy.members import MembersRepository, GymClassRepository
from cqrs.commands import ProfileTrainerCommand
from cqrs.handlers import ICommandHandler

from sqlalchemy.orm import Session


class DeleteMemberCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: MembersRepository = MembersRepository(sess)
    def handle(self, id:int) -> bool:
        result = self.repo.delete_member(id)
        return result
    

class DeleteGymClassCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: GymClassRepository = GymClassRepository(sess)
    def handle(self, id:int) -> bool:
        result = self.repo.delete_gym_class(id)
        return result