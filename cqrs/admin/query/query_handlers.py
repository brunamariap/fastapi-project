from repository.sqlalchemy.signup import SignupRepository
from cqrs.queries import SignupListQuery
from cqrs.handlers import IQueryHandler

from sqlalchemy.orm import Session


class SignupQueryHandler(IQueryHandler):
    def __init__(self, sess: Session):
        self.repo: SignupRepository = SignupRepository(sess)
        self.query: SignupListQuery = SignupListQuery()
    def handle(self) -> SignupListQuery:
        data = self.repo.get_all_signup()
        self.query.records = data
        return self.query


class GetSignupQuery(IQueryHandler):
    def __init__(self, sess: Session, id: int):
        self.repo: SignupRepository = SignupRepository(sess)
        self.query: SignupListQuery = SignupListQuery()
        self.id = id
    def handle(self) -> SignupListQuery:
        data = self.repo.get_signup(self.id)
        self.query.records = data
        return self.query