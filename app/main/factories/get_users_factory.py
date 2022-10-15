from app.services.usecases.users import GetUsers
from app.infra.data.repositories.users import UsersRepository
from app.infra.data.config import CSVFileManager

def get_users_factory():
    file_manager_instance = CSVFileManager(
        'D:/users/pichau/devprojects/training/python/fastapi-study/app/infra/data/tsf/users.tsv'
    )
    return GetUsers(
        users_repository=UsersRepository(file_manager_instance=file_manager_instance)
    )
