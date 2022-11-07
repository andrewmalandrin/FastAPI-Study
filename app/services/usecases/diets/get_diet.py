from typing import Dict

from app.domain.usecases.diets import GetDietContract, GetDietParams, GetDietResponse, Meal, Product

from app.services.contracts import DietsRepositoryContract, MealsRepositoryContract, MealProductsRepositoryContract,\
    ProductsRepositoryContract, UsersRepositoryContract, GetDietFileParams, GetMealProductsByFiltersParams
from app.services.contracts.meals_repository_contract import GetMealsByFiltersParams
from app.services.errors import DietNotFound, MealNotFound, MealProductNotFound, ProductNotFound
from app.services.helpers.http import HttpResponse, HttpStatus
from app.services.helpers.products import calculate_portion

class GetDiet(GetDietContract):
    def __init__(
        self,
        diets_repository: DietsRepositoryContract,
        meals_repository: MealsRepositoryContract,
        meal_products_repository: MealProductsRepositoryContract,
        products_repository: ProductsRepositoryContract,
        users_repository: UsersRepositoryContract
    ) -> None:
        self.diets_repository = diets_repository
        self.meals_repository = meals_repository
        self.meal_products_repository = meal_products_repository
        self.products_repository = products_repository
        self.users_repository = users_repository

    def _mount_response(self, diet: Dict, meals: Dict) -> GetDietResponse:
        
        response_meals = []
        
        for meal in meals:
            products = []
            for product in meal['products']:
                print('Meal Product', product)
                print('')
                print('')
                print('Product ID', product.get('id'))
                product_data = calculate_portion(
                    portion=product.get('portion'),
                    product=self.products_repository.get_product_by_filters(
                        product.get('product_id')
                    )
                )
                products.append(
                    Product(
                        id=product.get('product_id'),
                        name=product_data['name'],
                        portion=product.get('portion'),
                        carbohidrates=product_data['carbohidrates'],
                        proteins=product_data['proteins'],
                        fat=product_data['fat'],
                        saturated_fat=product_data['saturated_fat']
                    )
                )

            response_meals.append(Meal(
                    description=meal.get('description'),
                    products=products
                )
            )


        return GetDietResponse(
            id=diet.get('id'),
            meals=response_meals
        )

    def execute(self, params: GetDietParams) -> HttpResponse[GetDietResponse]:

        try:
            diet = self.diets_repository.get_diet_by_filters(
                GetDietFileParams(params.id)
            )
        except DietNotFound:
            return HttpStatus.not_found_404(
                'Diet not found'
            )

        try:
            meals = self.meals_repository.get_meals_by_filters(
                GetMealsByFiltersParams(
                    diet_id=diet.get('id')
                )
            )
        except MealNotFound:
            return HttpStatus.not_found_404(
                'Meal not found'
            )

        print('\n\n--------Meals: ', meals)

        
        try:
            for meal in meals:
                meal['products'] = self.meal_products_repository.get_meal_products_by_filters(
                    GetMealProductsByFiltersParams(
                        meal_id=meal['id']
                    )
                )
        except MealProductNotFound:
            return HttpStatus.not_found_404(
                'Meal product not found'
            )

            

        response = self._mount_response(diet, meals)

        return HttpStatus.ok_200(
            response
        )
