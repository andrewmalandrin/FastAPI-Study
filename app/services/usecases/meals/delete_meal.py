from app.domain.usecases import DeleteMealContract, DeleteMealParams
from app.services.contracts import MealProductsRepositoryContract, MealsRepositoryContract, GetMealProductsByFiltersParams
from app.services.errors import MealProductNotFound, MealNotFound
from app.services.helpers.http.http import HttpResponse, HttpStatus

class DeleteMeal(DeleteMealContract):

    def __init__(
            self,
            meals_repository: MealsRepositoryContract,
            meal_products_repository: MealProductsRepositoryContract
        ):
            self.meals_repository = meals_repository
            self.meal_products_repository = meal_products_repository

    def execute(self, params: DeleteMealParams) -> HttpResponse[str]:
        try:
            meal_products = self.meal_products_repository.get_meal_product_by_filters(
                GetMealProductsByFiltersParams(
                    meal_id=params.id
                )
            )
            for meal_product in meal_products:
                meal_product_id = meal_product['id']
                meal_product_message = self.meal_products_repository.delete_meal_product_by_filters(
                    id=meal_product_id
                )

                print(meal_product_message)

        except MealProductNotFound:
            return HttpStatus.not_found_404(
                f'Meal product id {meal_product_id} not found'
            )
        
        try:
            response = self.meals_repository.delete_meal(id=params.id)
        except MealNotFound:
            return HttpStatus.not_found_404(
                f'Meal id {params.id} not found'
            )
        
        return HttpStatus.accepted_202(
            response
        )
