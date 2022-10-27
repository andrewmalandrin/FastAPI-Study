from app.domain.usecases import UpdateDietContract, UpdateDietParams, UpdateDietResponse
from app.services.contracts import DietsRepositoryContract, MealsRepositoryContract, MealProductsRepositoryContract,\
    ProductsRepositoryContract, UsersRepositoryContract, UpdateDietFileParams
from app.services.errors import DietNotFound
from app.services.helpers.http import HttpResponse, HttpStatus

class UpdateDiet(UpdateDietContract):
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


    def execute(self, params: UpdateDietParams) -> HttpResponse[UpdateDietResponse]:
        
        if params.description:
        
            try:
                diet_data = self.diets_repository.update_diet(
                    UpdateDietFileParams(
                        id=params.id,
                        description=params.description
                    )
                )
            except DietNotFound:
                return HttpStatus.not_found_404(f'Diet id {params.id} not found')
            else:
                return HttpStatus.accepted_202(
                    UpdateDietResponse(
                        id=diet_data['id'],
                        description=diet_data['description']
                    )
                )
