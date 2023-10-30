from repository.sqlalchemy.trainers import TrainerRepository
from cqrs.commands import ProfileTrainerCommand
from cqrs.handlers import ICommandHandler
from fastapi import Depends

from db_config.sqlalchemy_connect import SessionFactory
from sqlalchemy.orm import Session


class AddLoginCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: TrainerRepository = TrainerRepository(sess)
    def handle(self, command: ProfileTrainerCommand) -> bool:
        result = self.repo.insert_trainer(command.details)
        return result