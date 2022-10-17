from typing import List
from app.services.contracts import SaveUserParams, UsersRepositoryContract
from app.infra.data.repositories.helpers import BaseRepository
from app.services.helpers.users import mount_users_data


class UsersRepository(BaseRepository, UsersRepositoryContract):
    def __init__(self, file_manager_instance):
        super().__init__(
            file_manager_instance=file_manager_instance
        )

    def create_user(self, params: SaveUserParams):
        user = []

        user.append(str(params.id))
        user.append(params.name)
        user.append(str(params.weight))
        user.append(str(params.carbo_kg))
        user.append(str(params.fat_kg))
        user.append(str(params.age))

        line = '\t'.join(user)
        line += '\n'

        self.file_manager_instance.add_line_to_tsv_file(line=line)

        return SaveUserParams(
            id=params.id,
            name=params.name,
            weight=params.weight,
            carbo_kg=params.carbo_kg,
            fat_kg=params.fat_kg,
            age=params.age
        )

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
