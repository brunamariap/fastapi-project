from sqlalchemy.orm import Session
from typing import Dict, Any

from domain.data.sqlalchemy_models import Profile_Members, Gym_Class


class GymClassRepository:
    def __init__(self, sess: Session):
        self.sess : Session = sess

    def insert_gym_class(self, member):
        try:
            self.sess.add(member)
            self.sess.commit()
            print(member.id)
        except:
            return False
        return True
    
    def update_gym_class(self, id:int, details: Dict[str, Any]) -> bool:
        try:
            self.sess.query(Gym_Class).filter(Gym_Class.id == id).update(details)
            self.sess.commit()

        except:
            return False
        return True
    
    def delete_gym_class(self, id: int) -> bool:
        try:
            gym_class = self.sess.query(Gym_Class).filter(Gym_Class.id == id).delete()
            self.sess.commit()

        except:
            return False
        return True
    
    def get_gym_class(self):
        return self.sess.query(Gym_Class).all()
    
    def get_gym_class(self):
        return self.sess.query(Gym_Class).filter(Gym_Class.id == id).one_or_none()


class MembersRepository:
    def __init__(self, sess: Session):
        self.sess : Session = sess

    def insert_member(self, member):
        try:
            self.sess.add(member)
            self.sess.commit()
            print(member.id)
        except:
            return False
        return True
    
    def update_member(self, id:int, details: Dict[str, Any]) -> bool:
        try:
            self.sess.query(Profile_Members).filter(Profile_Members.id == id).update(details)
            self.sess.commit()

        except:
            return False
        return True
    
    def delete_member(self, id: int) -> bool:
        try:
            member = self.sess.query(Profile_Members).filter(Profile_Members.id == id).delete()
            self.sess.commit()

        except:
            return False
        return True
    
    def get_all_members(self):
        return self.sess.query(Profile_Members).all()
    
    def get_member(self):
        return self.sess.query(Profile_Members).filter(Profile_Members.id == id).one_or_none()
