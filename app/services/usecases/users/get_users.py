from typing import List

from app.services.contracts import UsersRepositoryContract, UsersData
from app.domain.usecases.users import GetUsersContract, User, GetUsersResponse
from app.services.helpers.http import HttpResponse
from app.services.helpers.http.http import HttpStatus





class GetUsers(GetUsersContract):
    def __init__(
        self,
        users_repository: UsersRepositoryContract
    ):
        self.users_repository = users_repository

    def _mount_users_response(self, users_data: List) -> GetUsersResponse:
        users = []

        for user in users_data:
            users.append(
                User(
                    id=user['id'],
                    name=user['name'],
                    weight=user['weight'],
                    carbo_kg=user['carbo_kg'],
                    fat_kg=user['fat_kg'],
                    age=user['age']
                )
            )

        return GetUsersResponse(
            users=users
        )

    def execute(self, params) -> HttpResponse[GetUsersResponse]:

        users_data = self.users_repository.get_users()

        users = self._mount_users_response(
            users_data=users_data
        )

        return HttpStatus.ok_200(
            users
        )
