from app.domain.usecases import Usecase
from app.services.usecases.users import DeleteUser
from app.infra.data.repositories.users import UsersRepository
from app.infra.data.config import CSVFileManager
from app.services.enums import PathsEnum

def delete_user_factory() -> Usecase:
    file_manager_instance = CSVFileManager(
        file_path=PathsEnum.USERS_PATH
    )
    return DeleteUser(
        users_repository=UsersRepository(
            file_manager_instance=file_manager_instance
        )
    )
