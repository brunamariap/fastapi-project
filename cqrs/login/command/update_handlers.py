from repository.sqlalchemy.login import LoginRepository
from cqrs.commands import LoginCommand
from cqrs.handlers import ICommandHandler

from sqlalchemy.orm import Session


class UpdateLoginCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: LoginRepository = LoginRepository(sess)
    def handle(self, id:int, command: LoginCommand) -> bool:
        print("whdsbh")
        result = self.repo.update_login(id, command.details)
        return result