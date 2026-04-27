from dataclasses import dataclass
from datetime import datetime

from requests import Session


@dataclass
class User:
    firstname: str
    lastname: str
    email: str
    password: str
    title: str
    birthdate: datetime
    country: str
    state: str
    city: str
    address: str
    zipcode: str
    mobile_number: str


class UserApi:
    BASE_URL = "https://automationexercise.com/api"

    def __init__(self) -> None:
        self.__session = Session()

    def create_one(self, user: User) -> None:
        self.__session.post(
            url=f"{self.BASE_URL}/createAccount",
            data={
                "name": f"{user.firstname} {user.lastname}",
                "email": user.email,
                "password": user.password,
                "title": user.title,
                "birth_date": user.birthdate.day,
                "birth_month": user.birthdate.month,
                "birth_year": user.birthdate.year,
                "firstname": user.firstname,
                "lastname": user.lastname,
                "country": user.country,
                "state": user.state,
                "city": user.city,
                "address1": user.address,
                "address2": "",
                "zipcode": user.zipcode,
                "mobile_number": user.mobile_number,
            },
        )

    def delete_one(self, user: User) -> None:
        self.__session.delete(
            url=f"{self.BASE_URL}/deleteAccount",
            data={
                "email": user.email,
                "password": user.password,
            },
        )

    def delete_many(self, users: list[User]) -> None:
        for user in users:
            self.delete_one(user)
