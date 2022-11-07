from typing import List, Dict

from app.domain.usecases import CreateMealContract, CreateMealParams, CreateMealResponse, ProductParams
from app.services.contracts import MealsRepositoryContract, MealProductsRepositoryContract, ProductsRepositoryContract,\
    SaveMealProductParams, SaveMealParams
from app.services.errors import ProductNotFound
from app.services.helpers.http import HttpResponse, HttpStatus

class CreateMeal(CreateMealContract):
    def __init__(
        self,
        meals_repository: MealsRepositoryContract,
        meal_products_repository: MealProductsRepositoryContract,
        products_repository: ProductsRepositoryContract
    ) -> None:

        self.meals_repository = meals_repository
        self.meal_products_repository = meal_products_repository
        self.products_repository = products_repository

    def _validate_product(self, product: ProductParams) -> bool:
        try:
            self.products_repository.get_product_by_filters(id=product.id)
        except Exception as error:
            raise ProductNotFound from error
        return True

    def _mount_response(self, meal: Dict, meal_products: List[Dict]) -> CreateMealResponse:
        meal_products_response = []

        for meal_product in meal_products:
            product_name = self.products_repository.get_product_by_filters(
                id=meal_product['product_id']
            )['name']

            meal_products_response.append(
                ProductParams(
                    product_id=meal_product['product_id'],
                    name=product_name,
                    portion=meal_product['portion']
                )
            )

        return CreateMealResponse(
            id=meal['id'],
            diet_id=meal['diet_id'],
            products=meal_products_response
        )

    def execute(self, params: CreateMealParams) -> HttpResponse[CreateMealResponse]:

        for product in params.products:
            try:
                self._validate_product(product)
            except ProductNotFound:
                return HttpStatus.not_found_404(f'Product ID {product.id} not found')

        meal = self.meals_repository.create_meal(
            SaveMealParams(
                diet_id=params.diet_id,
                description=params.description
            )
        )

        meal_products = []

        for product in params.products:

            meal_products.append(
                self.meal_products_repository.save_meal_product(
                    SaveMealProductParams(
                        meal_id=meal['id'],
                        product_id=product.product_id,
                        portion=product.portion
                    )
                )
            )

        return HttpStatus.accepted_202(
            self._mount_response(
                meal=meal,
                meal_products=meal_products
            )
        )
