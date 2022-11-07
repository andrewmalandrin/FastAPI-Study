from app.services.usecases.meals import CreateMeal
from app.domain.usecases import Usecase
from app.infra.data.config import CSVFileManager
from app.infra.data.repositories.products import ProductsRepository
from app.infra.data.repositories.meals import MealsRepository, MealProductsRepository
from app.services.enums import PathsEnum

def create_meal_factory() -> Usecase:
    return CreateMeal(
        meals_repository=MealsRepository(file_manager_instance=CSVFileManager(PathsEnum.MEALS_PATH)),
        meal_products_repository=MealProductsRepository(file_manager_instance=CSVFileManager(PathsEnum.MEAL_PRODUCTS_PATH)),
        products_repository=ProductsRepository(file_manager_instance=CSVFileManager(PathsEnum.PRODUCTS_PATH)),
    )
