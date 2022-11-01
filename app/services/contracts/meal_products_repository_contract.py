from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

@dataclass
class DeleteMealProductFileParams:
    id: Optional[int] = None
    meal_id: Optional[int] = None

@dataclass
class UpdateMealProductFileParams:
    id: int
    portion: int

@dataclass
class GetMealProductsByFiltersParams:
    id: Optional[int] = None
    meal_id: Optional[int] = None

@dataclass
class GetMealProductByFiltersParams:
    id: int

@dataclass
class SaveMealProductParams:
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

    @abstractmethod
    def get_meal_products_by_filters(self, params: GetMealProductsByFiltersParams):
        raise NotImplementedError()

    @abstractmethod
    def update_meal_product(self, params: UpdateMealProductFileParams):
        raise NotImplementedError()

    @abstractmethod
    def delete_meal_product_by_filters(self, params: DeleteMealProductFileParams) -> str:
        raise NotImplementedError()
