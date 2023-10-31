from typing import List
from domain.data.sqlalchemy_models import Profile_Trainers, Login, Signup, Profile_Members, Attendance_Member, Gym_Class


class SignupListQuery:
    def __init__(self):
        self._records: List[Signup] = list()

    @property
    def records(self):
        return self._records
    
    @records.setter
    def records(self, records):
        self._records = records


class LoginListQuery:
    def __init__(self) -> None:
        self._records: List[Login] = list()

    @property
    def records(self):
        return self._records
    
    @records.setter
    def records(self, records):
        self._records = records


class ProfileTrainerListQuery:
    def __init__(self):
        self._records: List[Profile_Trainers] = list()

    @property
    def records(self):
        return self._records
    
    @records.setter
    def records(self, records):
        self._records = records


class ProfileMemberListQuery:
    def __init__(self):
        self._records: List[Profile_Members] = list()

    @property
    def records(self):
        return self._records
    
    @records.setter
    def records(self, records):
        self._records = records


class AttendanceListQuery:
    def __init__(self):
        self._records: List[Attendance_Member] = list()

    @property
    def records(self):
        return self._records
    
    @records.setter
    def records(self, records):
        self._records = records


class GymClassListQuery:
    def __init__(self):
        self._records: List[Gym_Class] = list()

    @property
    def records(self):
        return self._records
    
    @records.setter
    def records(self, records):
        self._records = records