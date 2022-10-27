from typing import List

from app.services.contracts import MealsRepositoryContract, GetMealByFiltersParams, GetMealsByFiltersParams, SaveMealParams
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
