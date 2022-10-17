from typing import List
from app.services.contracts import SaveUserParams, UpdateUserParams, UsersRepositoryContract
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
    
    def update_user(self, params: UpdateUserParams):
        user_data = self.get_user_by_filters(
            id=params.id
        )
        print('User data: ', user_data)

        file = self.file_manager_instance.read_tsv_file()

        user = []

        user.append(str(params.id))
        user.append(user_data['name'])
        
        items = params.__dict__.items()

        for item in items:
            if items[item] is not None:
                user.append(items[item])
            else:
                user.append(user_data[item])

        line = '\t'.join(user)
        line += '\n'

        print('New line: ', line)
        index = None
        
        for idx, line in file:
            if line[0] == params.id:
                index = idx

        self.file_manager_instance.update_tsv_file_line(
            file=file,
            new_line=user,
            index=index
        )

        return user
