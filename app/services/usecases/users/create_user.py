from app.domain.usecases.users import CreateUserCrontract, CreateUserParams, CreateUserResponse
from app.services.contracts import UsersRepositoryContract, SaveUserParams
from app.services.helpers.http import HttpResponse, HttpStatus

class CreateUser(CreateUserCrontract):
    def __init__(
        self,
        users_repository: UsersRepositoryContract
    ):
        self.users_repository = users_repository

    def execute(self, params: CreateUserParams) -> HttpResponse[CreateUserResponse]:
        
        try:
            user_id = self.users_repository.get_users()[-1]['id'] + 1
        except Exception:
            print('Nenhum usuário encontrado, criando o primeiro.')
            user_id = 1

        print('New user ID: ', user_id)

        created_user = self.users_repository.create_user(
            SaveUserParams(
                id=user_id,
                name=params.name,
                weight=params.weight,
                carbo_kg=params.carbo_kg,
                fat_kg=params.fat_kg,
                age=params.age
            )
        )


        return HttpStatus.created_201(
            CreateUserResponse(
                id=created_user.id,
                name=created_user.name,
                weight=created_user.weight,
                carbo_kg=created_user.carbo_kg,
                fat_kg=created_user.fat_kg,
                age=created_user.age
            )
        )
