from repository.sqlalchemy.trainers import TrainerRepository
from cqrs.commands import ProfileTrainerCommand
from cqrs.handlers import ICommandHandler

from sqlalchemy.orm import Session


class DeleteTrainerCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: TrainerRepository = TrainerRepository(sess)
    def handle(self, id:int) -> bool:
        result = self.repo.delete_trainer(id)
        return result