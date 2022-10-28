from typing import List

from app.services.contracts import MealProductsRepositoryContract, GetMealProductByFiltersParams, GetMealProductsByFiltersParams,\
    SaveMealProductParams, UpdateMealProductFileParams
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
        meal_products = mount_meal_products_data(self.file_manager_instance.read_tsv_file())
        
        filters = [
            [
                'id', params.id
            ]
        ]

        try:
            result = self._load_by_filters(filters=filters, data=meal_products)
            print('Meal products filter result: ', result)
            return result[0]
        except Exception as error:
            raise MealProductNotFound() from error

    def save_meal_product(self, params: SaveMealProductParams):
        meal_product = []

        try:
            id = self.get_meal_products()[-1]['id'] + 1
        except Exception as error:
            id = 1

        meal_product.append(str(id))
        meal_product.append(str(params.meal_id))
        meal_product.append(str(params.product_id))
        meal_product.append(str(params.portion))

        line = '\t'.join(meal_product)
        line += '\n'

        self.file_manager_instance.add_line_to_tsv_file(line=line)

        return {
            'id': id,
            'meal_id': params.meal_id,
            'product_id': params.product_id,
            'portion': params.portion
        }

    def get_meal_products_by_filters(self, params: GetMealProductsByFiltersParams) -> List:
        meal_products = mount_meal_products_data(self.file_manager_instance.read_tsv_file())
        
        filters = []

        if params.id:
            filters.append(['id', params.id])

        if params.meal_id:
            filters.append(['meal_id', params.meal_id])

        try:
            result = self._load_by_filters(filters=filters, data=meal_products)
            print('Meal products filter result: ', result)
            return result
        except Exception as error:
            raise MealProductNotFound() from error

    def update_meal_product(self, params: UpdateMealProductFileParams):
        meal_products_data = mount_meal_products_data(self.file_manager_instance.read_tsv_file())

        filters = [
            ['id', params.id]
        ]

        try:
            meal_product_data = self._load_by_filters(filters=filters, data=meal_products_data)[0]

            file = self.file_manager_instance.read_tsv_file()

            meal_product = []

            meal_product.append(str(params.id))
            meal_product.append(str(meal_product_data.get('meal_id')))
            meal_product.append(str(meal_product_data.get('product_id')))
            meal_product.append(str(params.portions))

        except Exception as error:
            raise MealProductNotFound() from error

        index = None

        for idx, line in enumerate(file):
            if line[0] == str[params.id]:
                index = idx

        self.file_manager_instance.update_tsv_file_line(
            file=file,
            new_line=meal_product,
            index=index
        )

        return {
            'id': meal_product[0],
            'meal_id': meal_product[1],
            'product_id': meal_product[2],
            'portion': meal_product[3]
        }
