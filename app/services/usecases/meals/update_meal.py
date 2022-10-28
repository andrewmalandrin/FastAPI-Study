from app.domain.usecases import UpdateMealContract, UpdateMealParams, UpdateMealResponse
from app.services.contracts import MealsRepositoryContract, UpdateMealFileParams
from app.services.errors import MealNotFound
from app.services.helpers.http import HttpResponse
from app.services.helpers.http.http import HttpStatus

class UpdateMeal(UpdateMealContract):
    def __init__(self,
    meals_repository: MealsRepositoryContract
    ):
        self.meals_repository = meals_repository

    def execute(self, params: UpdateMealParams) -> HttpResponse[UpdateMealResponse]:
        try:
            meal = self.meals_repository.update_meal(
                UpdateMealFileParams(
                    id=params.id,
                    description=params.description
                )
            )
        except MealNotFound:
            return HttpStatus.not_found_404('Meal not founud')

        return HttpStatus.accepted_202(
            UpdateMealResponse(
                id=meal.get('id'),
                description=meal.get('description')
            )
        )