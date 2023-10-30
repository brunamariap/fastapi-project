from repository.sqlalchemy.trainers import TrainerRepository
from cqrs.queries import ProfileTrainerListQuery
from cqrs.handlers import IQueryHandler

from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import SessionFactory


class ListTrainerQueryHandler(IQueryHandler):
    def __init__(self, sess: Session):
        self.repo: TrainerRepository = TrainerRepository(sess)
        self.query: ProfileTrainerListQuery = ProfileTrainerListQuery()
    def handle(self) -> ProfileTrainerListQuery:
        data = self.repo.get_all_trainers()
        self.query.records = data
        return self.query
    

class GetTrainerQueryHandler(IQueryHandler):
    def __init__(self, sess: Session, id: int):
        self.repo: TrainerRepository = TrainerRepository(sess)
        self.query: ProfileTrainerListQuery = ProfileTrainerListQuery()
        self.id = id
    def handle(self) -> ProfileTrainerListQuery:
        data = self.repo.get_trainer(self.id)
        self.query.records = data
        return self.query