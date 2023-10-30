from repository.sqlalchemy.login import LoginRepository
from cqrs.handlers import ICommandHandler

from sqlalchemy.orm import Session


class DeleteLoginCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: LoginRepository = LoginRepository(sess)
    def handle(self, id:int) -> bool:
        result = self.repo.delete_login(id)
        return result