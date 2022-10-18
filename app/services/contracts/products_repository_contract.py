from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class CreateProductParams:
    name: str
    portion: int
    portion_unity: str
    carbo: float
    prot: float
    fat: float
    saturated_fat: float

@dataclass
class GetProductParams:
    id: str
    portion: Optional[int] = None

@dataclass
class ProductsData:
    id: int
    name: str
    portion: int
    portion_unity: str
    carbo: float
    prot: float
    fat: float
    saturated_fat: float

class ProductsRepositoryContract(ABC):
    @abstractmethod
    def create_product(self, params: CreateProductParams) -> ProductsData:
        raise NotImplementedError()

    @abstractmethod
    def get_products(self) -> List:
        raise NotImplementedError()
        
    @abstractmethod
    def get_product_by_filters(self, id: str) -> List:
        raise NotImplementedError()

