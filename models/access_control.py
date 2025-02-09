from pydantic import HttpUrl

class Grant():
    def __init__(self, user: HttpUrl, role: str) -> None:
        self.user = user
        self.role = role

    @property
    def user(self) -> HttpUrl:
        return self._user

    @user.setter
    def user(self, user: HttpUrl):
        self._user = user

    @property
    def role(self) -> str:
        return self._role

    @role.setter
    def role(self, role: str):
        self._role = role

    def __repr__(self):
        return f"Grant({self.user}, {self.role})"
