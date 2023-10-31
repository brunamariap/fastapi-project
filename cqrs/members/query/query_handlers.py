from repository.sqlalchemy.members import MembersRepository, GymClassRepository
from cqrs.queries import ProfileMemberListQuery, GymClassListQuery 
from cqrs.handlers import IQueryHandler

from sqlalchemy.orm import Session


class ListMembersQueryHandler(IQueryHandler):
    def __init__(self, sess: Session):
        self.repo: MembersRepository = MembersRepository(sess)
        self.query: ProfileMemberListQuery = ProfileMemberListQuery()
    def handle(self) -> ProfileMemberListQuery:
        data = self.repo.get_all_members()
        self.query.records = data
        return self.query
    

class GetMemberQueryHandler(IQueryHandler):
    def __init__(self, sess: Session, id: int):
        self.repo: MembersRepository = MembersRepository(sess)
        self.query: ProfileMemberListQuery = ProfileMemberListQuery()
        self.id = id
    def handle(self) -> ProfileMemberListQuery:
        data = self.repo.get_member(self.id)
        self.query.records = data
        return self.query
    

class ListGymClassQueryHandler(IQueryHandler):
    def __init__(self, sess: Session):
        self.repo: GymClassRepository = GymClassRepository(sess)
        self.query: GymClassListQuery = GymClassListQuery()
    def handle(self) -> GymClassListQuery:
        data = self.repo.get_gym_class()
        self.query.records = data
        return self.query
    

class GetGymClassQueryHandler(IQueryHandler):
    def __init__(self, sess: Session, id: int):
        self.repo: GymClassRepository = GymClassRepository(sess)
        self.query: GymClassListQuery = GymClassListQuery()
        self.id = id
    def handle(self) -> GymClassListQuery:
        data = self.repo.get_member(self.id)
        self.query.records = data
        return self.query