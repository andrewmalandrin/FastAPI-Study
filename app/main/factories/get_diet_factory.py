from app.services.usecases.diets import GetDiet
from app.domain.usecases import Usecase
from app.infra.data.config import CSVFileManager
from app.infra.data.repositories.products import ProductsRepository
from app.infra.data.repositories.diets import DietsRepository
from app.infra.data.repositories.meals import MealsRepository, MealProductsRepository
from app.infra.data.repositories.users import UsersRepository
from app.services.enums import PathsEnum

def get_diet_factory() -> Usecase:
    return GetDiet(
        diets_repository=DietsRepository(file_manager_instance=CSVFileManager(PathsEnum.DIETS_PATH)),
        meals_repository=MealsRepository(file_manager_instance=CSVFileManager(PathsEnum.MEALS_PATH)),
        meal_products_repository=MealProductsRepository(file_manager_instance=CSVFileManager(PathsEnum.MEAL_PRODUCTS_PATH)),
        products_repository=ProductsRepository(file_manager_instance=CSVFileManager(PathsEnum.PRODUCTS_PATH)),
        users_repository=UsersRepository(file_manager_instance=CSVFileManager(PathsEnum.USERS_PATH))
    )
