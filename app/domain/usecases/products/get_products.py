from abc import abstractmethod
from typing import List
from pydantic import BaseModel, Field
from app.domain.usecases import Usecase

class Product(BaseModel):
    id: int
    name: str
    portion: int
    portion_unity: str = Field(alias='portionUnity')
    carbo: float
    prot: float
    fat: float
    saturated_fat: float = Field(alias='saturatedFat')

    class Config:
        allow_population_by_field_name = True

class GetProductsResponse(BaseModel):
    products: List[Product]

class GetProductsContract(Usecase):
    @abstractmethod
    def execute(self):
        raise NotImplementedError