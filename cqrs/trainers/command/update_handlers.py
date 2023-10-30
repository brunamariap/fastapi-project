from repository.sqlalchemy.trainers import TrainerRepository
from cqrs.commands import ProfileTrainerCommand
from cqrs.handlers import ICommandHandler

from sqlalchemy.orm import Session


class UpdateTrainerCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: TrainerRepository = TrainerRepository(sess)
    def handle(self, id:int, command: ProfileTrainerCommand) -> bool:
        result = self.repo.update_trainer(id, command.details)
        return result