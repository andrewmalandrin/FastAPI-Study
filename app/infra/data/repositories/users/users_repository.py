from typing import List
from unicodedata import name
from app.domain.usecases.users.update_user import UpdateUserParams
from app.services.contracts import SaveUserParams, UpdateFileUserParams, UsersRepositoryContract
from app.infra.data.repositories.helpers import BaseRepository
from app.services.contracts import UsersData
from app.services.errors import UserNotFound
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
        try:
            users = mount_users_data(self.file_manager_instance.read_tsv_file())

            filters = [
                [
                    'id',id
                ]
            ]

            result = self._load_by_filters(filters, users)

            return result[0]
        except Exception as error:
            raise UserNotFound() from error
    
    def update_user(self, params: UpdateFileUserParams):
        try:
            user_data = self.get_user_by_filters(
                id=int(params.id)
            )
            print('User data: ', user_data)
        except UserNotFound:
            raise UserNotFound()

        file = self.file_manager_instance.read_tsv_file()
        print('File: ', file)

        user = []

        user.append(str(params.id))
        user.append(user_data['name'])
        
        items = params.__dict__

        if items['id']:
            del items['id']
        for item in items:
            
            if items[item] is not None:
                print('Item: ', item)
                user.append(str(items[item]))
            else:
                user.append(str(user_data[item]))

        index = None
        
        for idx, line in enumerate(file):
            if line[0] == user[0]:
                index = idx

        self.file_manager_instance.update_tsv_file_line(
            file=file,
            new_line=user,
            index=index
        )

        print('User: ', user)
        return {
            'id': int(user[0]),
            'name': user[1],
            'weight': float(user[2]),
            'carbo_kg': float(user[3]),
            'fat_kg': float(user[4]),
            'age': int(user[5])
        }
