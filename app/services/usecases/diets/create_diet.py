from typing import Dict

from app.domain.usecases import CreateDietContract, CreateDietParams, CreateDietResponse, Meals, Products

from app.services.contracts import DietsRepositoryContract, MealsRepositoryContract, MealProductsRepositoryContract, SaveDietFileParams,\
    SaveMealParams, SaveMealProductParams, ProductsRepositoryContract, UsersRepositoryContract
from app.services.helpers.http import HttpResponse
from app.services.helpers.http.http import HttpStatus

class CreateDiet(CreateDietContract):
    def __init__(
        self,
        diets_repository: DietsRepositoryContract,
        meals_repository: MealsRepositoryContract,
        meal_products_repository: MealProductsRepositoryContract,
        products_repository: ProductsRepositoryContract,
        users_repository: UsersRepositoryContract
    ):

        self.diets_repository = diets_repository
        self.meals_repository = meals_repository
        self.meal_products_repository = meal_products_repository
        self.products_repository = products_repository
        self.users_repository = users_repository

    def _mount_response(self, diet: Dict, meals: Dict) -> CreateDietResponse:

        response_meals = []
        for meal in meals:
            products = []
            for product in meal['products']:
                products.append(
                    Products(
                        product_id=product.get('product_id'),
                        name=product.get('name'),
                        portion=product.get('portion')
                    )
                )

            response_meals.append(
                Meals(
                    description=meal.get('description'),
                    products=products
                )
            )

        diet_response = CreateDietResponse(
            diet_id=diet.get('id'),
            user_id=diet.get('user_id'),
            user_name=self.users_repository.get_user_by_filters(diet.get('user_id')),
            meals=response_meals
        )
        return diet_response


    def execute(self, params: CreateDietParams) -> HttpResponse[CreateDietResponse]:
        diet = self.diets_repository.create_diet(
            SaveDietFileParams(
                user_id=params.user_id,
                description=params.description
            )
        )
        meals = []
        for meal in params.meals:
            current_meal = self.meals_repository.create_meal(
                SaveMealParams(
                    diet_id=diet.get('id'),
                    description=meal.description
                )
            )
            current_meal['products'] = []
            for product in meal.products:
                current_product = self.meal_products_repository.save_meal_product(
                    SaveMealProductParams(
                        meal_id=current_meal.get('id'),
                        product_id=product.product_id,
                        portion=product.portion
                    )
                )
                current_product['name'] = self.products_repository.get_product_by_filters(
                    id=product.product_id
                ).get('name')

                current_meal['products'].append(current_product)

            meals.append(current_meal)

        response = self._mount_response(diet, meals)

        return HttpStatus.created_201(
            response
        )
