from typing import Dict, Any


class SignupCommand:
    def __init__(self):
        self._details: Dict[str, Any] = dict()

    @property
    def details(self):
        return self._details
    
    @details.setter
    def details(self, details):
        self._details = details


class LoginCommand:
    def __init__(self):
        self._details: Dict[str, Any] = dict()

    @property
    def details(self):
        return self._details
    
    @details.setter
    def details(self, details):
        self._details = details


class ProfileTrainerCommand:
    def __init__(self):
        self._details: Dict[str, Any] = dict()

    @property
    def details(self):
        return self._details
    
    @details.setter
    def details(self, details):
        self._details = details


class ProfileMemberCommand:
    def __init__(self):
        self._details: Dict[str, Any] = dict()

    @property
    def details(self):
        return self._details
    
    @details.setter
    def details(self, details):
        self._details = details


class AttendanceMemberCommand:
    def __init__(self):
        self._details: Dict[str, Any] = dict()

    @property
    def details(self):
        return self._details
    
    @details.setter
    def details(self, details):
        self._details = details


class GymClassCommand:
    def __init__(self):
        self._details: Dict[str, Any] = dict()

    @property
    def details(self):
        return self._details
    
    @details.setter
    def details(self, details):
        self._details = details