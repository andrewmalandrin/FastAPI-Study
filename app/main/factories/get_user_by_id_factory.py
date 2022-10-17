from app.services.usecases.users import GetUserById
from app.infra.data.repositories.users import UsersRepository
from app.infra.data.config import CSVFileManager
from app.services.enums import PathsEnum

def get_user_by_id_factory():
    file_manager_instance = CSVFileManager(
        PathsEnum.USERS_PATH
    )
    return GetUserById(
        users_repository=UsersRepository(file_manager_instance=file_manager_instance)
    )
