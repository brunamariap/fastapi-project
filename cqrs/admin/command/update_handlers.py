from repository.sqlalchemy.signup import SignupRepository
from cqrs.commands import SignupCommand
from cqrs.handlers import ICommandHandler

from sqlalchemy.orm import Session


class UpdateSignupCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: SignupRepository = SignupRepository(sess)
    def handle(self, id:int, command: SignupCommand) -> bool:
        result = self.repo.update_signup(id, command.details)
        return result