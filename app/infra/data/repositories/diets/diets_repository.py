from typing import List, Dict
from app.services.contracts import DietsRepositoryContract, GetDietFileParams, SaveDietFileParams
from app.infra.data.repositories.helpers import BaseRepository
from app.services.errors import DietNotFound
from app.services.helpers.diets import mount_diets_data

class DietsRepository(DietsRepositoryContract, BaseRepository):
    def __init__(self, file_manager_instance):
        super().__init__(
            file_manager_instance=file_manager_instance
        )

    def get_diets(self) -> List:
        diets = mount_diets_data(self.file_manager_instance.read_tsv_file())
        return diets

    def get_diet_by_filters(self, params: GetDietFileParams) -> Dict:
        diets = mount_diets_data(self.file_manager_instance.read_tsv_file())

        filters = [
            [
                'id', params.id
            ]
        ]

        try:
            result = self._load_by_filters(filters=filters)
            print('Diets filtered data: ', result)
            return result[0]
        except Exception as error:
            raise DietNotFound() from error
        

    def create_diet(self, params: SaveDietFileParams) -> Dict:
        diet = []

        try:
            id = int(self.get_diets()[-1]['id']) + 1
        except Exception as error:
            print('No diets found, creating first one.')
            id = 1

        diet.append(str(id))
        diet.append(str(params.user_id))
        diet.append(params.description)

        line = '\t'.join(diet)
        line += '\n'

        self.file_manager_instance.add_line_to_tsv_file(line=line)
        
        return {
            'id': id,
            'user_id': params.user_id,
            'description': params.description
        }
