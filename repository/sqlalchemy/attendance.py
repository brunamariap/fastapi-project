from sqlalchemy.orm import Session
from typing import Dict, Any

from domain.data.sqlalchemy_models import Attendance_Member


class AttendanceRepository:
    def __inti__(self, sess: Session):
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
            self.sess.query(Attendance_Member).filter(Attendance_Member.id == id).update(details)
            self.sess.commit()

        except:
            return False
        return True
    
    def delete_member(self, id: int) -> bool:
        try:
            member = self.sess.query(Attendance_Member).filter(Attendance_Member.id == id).delete()
            self.sess.commit()

        except:
            return False
        return True
    
    def get_all_members(self):
        return self.sess.query(Attendance_Member).all()
    
    def get_member(self):
        return self.sess.query(Attendance_Member).filter(Attendance_Member.id == id).one_or_none()
