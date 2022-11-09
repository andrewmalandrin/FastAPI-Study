from typing import Dict

from app.domain.usecases import CreateMealProductContract, CreateMealProductParams, CreateMealProductResponse
from app.services.contracts import MealProductsRepositoryContract, MealsRepositoryContract, ProductsRepositoryContract,\
    GetMealByFiltersParams, SaveMealProductParams
from app.services.errors import ProductNotFound, MealNotFound
from app.services.helpers.http import HttpResponse, HttpStatus

class CreateMealProduct(CreateMealProductContract):
    def __init__(
        self,
        meal_products_repository: MealProductsRepositoryContract,
        products_repository:  ProductsRepositoryContract,
        meals_repository: MealsRepositoryContract
    ) -> None:

        self.meal_products_repository = meal_products_repository
        self.products_repository = products_repository
        self.meals_repository = meals_repository

    def execute(self, params: CreateMealProductParams) -> HttpResponse[CreateMealProductResponse]:
        try:
            product = self.products_repository.get_product_by_filters(id=params.product_id)
            meal = self.meals_repository.get_meal_by_filters(
                GetMealByFiltersParams(id=params.meal_id)
            )
        except MealNotFound:
            return HttpStatus.not_found_404('Meal not found')
        except ProductNotFound:
            return HttpStatus.not_found_404('Product not found')

        meal_product = self.meal_products_repository.save_meal_product(
            SaveMealProductParams(
                meal_id=params.meal_id,
                product_id=params.product_id,
                portion=params.portion
            )
        )

        return HttpStatus.created_201(
            CreateMealProductResponse(
                id=meal_product['id'],
                meal_id=meal['id'],
                product_id=product['id'],
                product_name=product['name'],
                portion=meal_product['portion']
            )
        )
