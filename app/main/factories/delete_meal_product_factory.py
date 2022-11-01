from app.services.usecases.meals import DeleteMealProduct
from app.domain.usecases import Usecase
from app.infra.data.config import CSVFileManager
from app.infra.data.repositories.meals import MealProductsRepository
from app.services.enums import PathsEnum

def delete_meal_product_factory() -> Usecase:
    return DeleteMealProduct(
        meal_products_repository=MealProductsRepository(
            file_manager_instance=CSVFileManager(PathsEnum.MEAL_PRODUCTS_PATH)
        )
    )
