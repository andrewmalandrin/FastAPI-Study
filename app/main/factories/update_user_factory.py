from app.services.usecases.users import UpdateUser
from app.infra.data.repositories.users import UsersRepository
from app.infra.data.config import CSVFileManager
from app.services.enums import PathsEnum

def update_user_factory():
    file_manager_instance = CSVFileManager(
        PathsEnum.USERS_PATH
    )
    return UpdateUser(
        users_repository=UsersRepository(file_manager_instance=file_manager_instance)
    )
