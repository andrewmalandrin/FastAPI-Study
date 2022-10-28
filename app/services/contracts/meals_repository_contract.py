from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

@dataclass
class UpdateMealFileParams:
    id: int
    description: str

@dataclass
class GetMealsByFiltersParams:
    id: Optional[int] = None
    diet_id: Optional[int] = None
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

    @abstractmethod
    def get_meals_by_filters(self, params: GetMealsByFiltersParams):
        raise NotImplementedError()

    @abstractmethod
    def update_meal(self, params: UpdateMealFileParams):
        raise NotImplementedError()
