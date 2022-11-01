from app.domain.usecases import DeleteMealProductContract, DeleteMealProductParams,\
    DeleteMealProductResponse
from app.services.contracts import MealProductsRepositoryContract, DeleteMealProductFileParams
from app.services.errors import MealProductNotFound
from app.services.helpers.http.http import HttpResponse, HttpStatus

class DeleteMealProduct(DeleteMealProductContract):
    def __init__(
        self,
        meal_products_repository: MealProductsRepositoryContract
    ):
        self.meal_products_repository = meal_products_repository

    def execute(self, params: DeleteMealProductParams) -> HttpResponse[DeleteMealProductResponse]:
        try:
            self.meal_products_repository.delete_meal_product_by_filters(
                DeleteMealProductFileParams(
                    id=params.id
                )
            )
        except MealProductNotFound:
            return HttpStatus.not_found_404(
                f'Meal product id {params.id} not found'
            )

        return HttpStatus.accepted_202(
            DeleteMealProductResponse(
                f'Meal product id {params.id} deleted'
            )
        )
