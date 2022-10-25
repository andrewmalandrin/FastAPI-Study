from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class GetMealByFiltersParams:
    id: int

@dataclass
class SaveMealParams:
    diet_id: int
    description: str

class MealsRepositoryContract(ABC):
    @abstractmethod
    def get_meals(self):
        raise NotImplementedError()

    @abstractmethod
    def get_meal_by_filters(self, params: GetMealByFiltersParams):
        raise NotImplementedError()

    @abstractmethod
    def create_meal(self, params: SaveMealParams):
        raise NotImplementedError()
