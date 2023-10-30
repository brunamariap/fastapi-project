from repository.sqlalchemy.signup import SignupRepository
from cqrs.handlers import ICommandHandler

from sqlalchemy.orm import Session


class DeleteSignupCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: SignupRepository = SignupRepository(sess)
    def handle(self, id:int) -> bool:
        result = self.repo.delete_signup(id)
        return result