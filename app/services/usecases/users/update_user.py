from app.services.contracts import UsersRepositoryContract, UpdateFileUserParams
from app.domain.usecases.users import UpdateUserContract, UpdateUserParams, UpdateUserResponse
from app.services.helpers.http import HttpResponse
from app.services.helpers.http.http import HttpStatus

class UpdateUser(UpdateUserContract):
    def __init__(
        self,
        users_repository: UsersRepositoryContract
    ):
        self.users_repository = users_repository
    
    def execute(self, params: UpdateUserParams) -> HttpResponse[UpdateUserResponse]:
        
        user = self.users_repository.update_user(
            UpdateFileUserParams(
                id=params.id,
                weight=params.weight,
                carbo_kg=params.carbo_kg,
                fat_kg=params.fat_kg,
                age=params.age
            )
        )

        return HttpStatus.accepted_202(
            UpdateUserResponse(
                id=user['id'],
                name=user['name'],
                weight=user['weight'],
                carbo_kg=user['carbo_kg'],
                fat_kg=user['fat_kg'],
                age=user['age']
            )
        )
        