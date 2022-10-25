from app.services.contracts import MealProductsRepositoryContract, GetMealProductByFiltersParams, SaveMealProductParams
from app.infra.data.repositories.helpers import BaseRepository
from app.services.helpers.meals import mount_meal_products_data
from app.services.errors import MealProductNotFound

class MealProductsRepository(MealProductsRepositoryContract, BaseRepository):
    def __init__(self, file_manager_instance):
        super().__init__(
            file_manager_instance=file_manager_instance
        )

    def get_meal_products(self):
        return mount_meal_products_data(self.file_manager_instance.read_tsv_file())

    def get_meal_product_by_filters(self, params: GetMealProductByFiltersParams):
        filters = [
            [
                'id', params.id
            ]
        ]

        try:
            result = self._load_by_filters(filters=filters)
            print('Meal products filter result: ', result)
            return result
        except Exception as error:
            raise MealProductNotFound() from error

    def save_meal_product(self, params: SaveMealProductParams):
        meal_product = []

        try:
            id = self.get_meal_products()[-1]['id'] - 1
        except Exception as error:
            id = 1

        meal_product.append(id)
        meal_product.append(params.meal_id)
        meal_product.append(params.product_id)
        meal_product.append(params.portion)

        return {
            'id': id,
            'meal_id': params.meal_id,
            'product_id': params.product_id,
            'portion': params.portion
        }
