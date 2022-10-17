from app.domain.usecases.users import GetUserByIdContract, GetUserByIdParams, GetUserByIdResponse
from app.services.contracts import UsersRepositoryContract
from app.services.helpers.http import HttpResponse, HttpStatus


class GetUserById(GetUserByIdContract):
    def __init__(
        self,
        users_repository: UsersRepositoryContract
    ):
        self.users_repository = users_repository

    def execute(self, params: GetUserByIdParams) -> HttpResponse[GetUserByIdResponse]:
        user = self.users_repository.get_user_by_filters(id=params.id)

        return HttpStatus.ok_200(
            GetUserByIdResponse(
                id=user['id'],
                name=user['name'],
                weight=user['weight'],
                carbo_kg=user['carbo_kg'],
                fat_kg=user['fat_kg'],
                age=user['age']
            )
        )
