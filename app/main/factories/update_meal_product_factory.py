from app.services.usecases.meals import UpdateMealProduct
from app.domain.usecases import Usecase
from app.infra.data.config import CSVFileManager
from app.infra.data.repositories.meals import MealProductsRepository
from app.services.enums import PathsEnum

def update_meal_product_factory() -> Usecase:
    return UpdateMealProduct(
        meal_products_repository=MealProductsRepository(
            CSVFileManager(
                file_path=PathsEnum.MEAL_PRODUCTS_PATH
            )
        )
    )
