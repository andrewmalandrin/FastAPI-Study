from typing import List
from app.services.contracts import CreateUserParams, UsersRepositoryContract
from app.infra.data.repositories.helpers import BaseRepository
from app.services.helpers.users import mount_users_data


class UsersRepository(BaseRepository, UsersRepositoryContract):
    def __init__(self, file_manager_instance):
        super().__init__(
            file_manager_instance=file_manager_instance
        )
    # TODO: Desenvolver
    def create_user(self, params: CreateUserParams):
        return

    def get_users(self) -> List:
        return mount_users_data(self.file_manager_instance.read_tsv_file())

    def get_user_by_filters(self, id: int):
        users = mount_users_data(self.file_manager_instance.read_tsv_file())

        filters = [
            [
                'id',id
            ]
        ]

        result = self._load_by_filters(filters, users)

        return result[0]
