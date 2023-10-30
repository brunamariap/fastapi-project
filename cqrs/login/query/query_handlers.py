from repository.sqlalchemy.login import LoginRepository
from cqrs.queries import LoginListQuery
from cqrs.handlers import IQueryHandler

from sqlalchemy.orm import Session


class ListLoginQueryHandler(IQueryHandler):
    def __init__(self, sess: Session):
        self.repo: LoginRepository = LoginRepository(sess)
        self.query: LoginListQuery = LoginListQuery()
    def handle(self) -> LoginListQuery:
        data = self.repo.get_all_login()
        self.query.records = data
        return self.query


class GetLoginQueryHandler(IQueryHandler):
    def __init__(self, sess: Session, id: int):
        self.repo: LoginRepository = LoginRepository(sess)
        self.query: LoginListQuery = LoginListQuery()
        self.id = id
    def handle(self) -> LoginListQuery:
        data = self.repo.get_login(self.id)
        self.query.records = data
        return self.query