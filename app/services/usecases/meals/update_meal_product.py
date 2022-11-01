from app.domain.usecases import UpdateMealProductContract, UpdateMealProductParams, UpdateMealProductResponse
from app.services.contracts import MealProductsRepositoryContract, UpdateMealProductFileParams
from app.services.helpers.http import HttpResponse, HttpStatus
from app.services.errors import MealProductNotFound

class UpdateMealProduct(UpdateMealProductContract):
    def __init__(
        self,
        meal_products_repository: MealProductsRepositoryContract
    ) -> None:
        self.meal_products_repository = meal_products_repository

    def execute(self, params: UpdateMealProductParams) -> HttpResponse[UpdateMealProductResponse]:
        try:
            meal_product = self.meal_products_repository.update_meal_product(
                UpdateMealProductFileParams(
                    id=params.id,
                    portion=params.portion
                )
            )
        except MealProductNotFound:
            return HttpStatus.not_found_404(
                'Meal product not found'
            )

        return HttpStatus.accepted_202(
            UpdateMealProductResponse(
                id=meal_product.get('id'),
                portion=meal_product.get('portion')
            )
        )
