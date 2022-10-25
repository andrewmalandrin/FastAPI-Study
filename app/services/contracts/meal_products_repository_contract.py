from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class GetMealProductByFiltersParams:
    id: int

@dataclass
class SaveMealProductParams:
    id: int
    meal_id: int
    product_id: int
    portion: int

class MealProductsRepositoryContract(ABC):
    @abstractmethod
    def get_meal_products(self):
        raise NotImplementedError()

    @abstractmethod
    def get_meal_product_by_filters(self, params: GetMealProductByFiltersParams):
        raise NotImplementedError()

    @abstractmethod
    def save_meal_product(self, params: SaveMealProductParams):
        raise NotImplementedError()
