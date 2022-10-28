from app.services.usecases.meals import UpdateMeal
from app.domain.usecases import Usecase
from app.infra.data.config import CSVFileManager
from app.infra.data.repositories.meals import MealsRepository
from app.services.enums import PathsEnum

def update_meal_factory() -> Usecase:
    return UpdateMeal(
        meals_repository=MealsRepository(file_manager_instance=CSVFileManager(PathsEnum.MEALS_PATH))
    )
