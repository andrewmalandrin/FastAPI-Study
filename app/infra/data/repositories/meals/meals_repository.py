from typing import List, Dict

from app.services.contracts import MealsRepositoryContract, GetMealByFiltersParams, GetMealsByFiltersParams, SaveMealParams,\
    UpdateMealFileParams
from app.infra.data.repositories.helpers import BaseRepository
from app.services.helpers.meals import mount_meals_data
from app.services.errors import MealNotFound


class MealsRepository(MealsRepositoryContract, BaseRepository):
    def __init__(self, file_manager_instance):
        super().__init__(
            file_manager_instance=file_manager_instance
        )

    def get_meals(self):
        return mount_meals_data(self.file_manager_instance.read_tsv_file())

    def get_meal_by_filters(self, params: GetMealByFiltersParams):
        
        meal = mount_meals_data(self.file_manager_instance.read_tsv_file())

        filters = []

        filters.append(['id', params.id])
        
        try:
            result = self._load_by_filters(filters=filters, data=meal)
            print('Meals filter result: ')
            return result[0]
        except Exception as error:
            raise MealNotFound() from error

    def create_meal(self, params: SaveMealParams):
        meal = []
        
        try:
            id = self.get_meals()[-1]['id'] + 1
        except Exception as error:
            print('Meals not found, creating first one.')
            id = 1
        
        meal.append(str(id))
        meal.append(str(params.diet_id))
        meal.append(params.description)

        line = '\t'.join(meal)
        line += '\n'

        self.file_manager_instance.add_line_to_tsv_file(line=line)

        return {
            'id': id,
            'diet_id': params.diet_id,
            'description': params.description
        }

    def get_meals_by_filters(self, params: GetMealsByFiltersParams) -> List:

        meal = mount_meals_data(self.file_manager_instance.read_tsv_file())

        filters = []

        if params.id:
            filters.append(['id', params.id])

        if params.diet_id:
            filters.append(['diet_id', params.diet_id])

        try:
            result = self._load_by_filters(filters=filters, data=meal)
            print('Meals filter result: ')
            return result
        except Exception as error:
            raise MealNotFound() from error

    def update_meal(self, params: UpdateMealFileParams) -> Dict:

        meals_data = mount_meals_data(self.file_manager_instance.read_tsv_file())

        filters = []

        filters.append(
            ['id', params.id]
        )

        try:
            meal_data = self._load_by_filters(filters=filters, data=meals_data)[0]
            print('Meal filter result: ', meal_data)

            file = self.file_manager_instance.read_tsv_file()

            meal = []

            meal.append(str(params.id))
            meal.append(str(meal_data.get('diet_id')))
            meal.append(params.description)

        except Exception as error:
            raise MealNotFound() from error

        index = None

        for idx, line in enumerate(file):
            if line[0] == str(params.id):
                index = idx

        self.file_manager_instance.update_tsv_file_line(
            file=file,
            new_line=meal,
            index=index
        )

        return{
            'id': meal[0],
            'diet_id': meal[1],
            'description': meal[2]
        }

    def delete_meal(self, id: int) -> str:
        file = self.file_manager_instance.read_tsv_file()

        filters = ['id', id]

        meal = self._load_by_filters(
            filters=filters, data=mount_meals_data(file)
        )

        if not meal:
            raise MealNotFound()

        for idx, line in enumerate(file):
            if line[0] == str(id):
                index = idx
        
        self.file_manager_instance.delete_tsv_file_line(
            file=file,
            index=index
        )

        return 'Meal deleted successfully'
