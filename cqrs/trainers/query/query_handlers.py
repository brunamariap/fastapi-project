from repository.sqlalchemy.trainers import TrainerRepository
from cqrs.queries import ProfileTrainerListQuery
from cqrs.handlers import IQueryHandler

from fastapi import Depends
from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import SessionFactory

def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()


class ListTrainerQueryHandler(IQueryHandler):
    def __init__(self, sess: Session = Depends(sess_db)):
        # sess = Depends(sess_db)
        self.repo: TrainerRepository = TrainerRepository(sess)
        self.query: ProfileTrainerListQuery = ProfileTrainerListQuery()
    def handle(self) -> ProfileTrainerListQuery:
        data = self.repo.get_all_trainers()
        self.query.records = data
        return self.query