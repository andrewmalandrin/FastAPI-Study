from abc import abstractmethod
from typing import List
from pydantic import BaseModel, Field
from app.services.helpers.string import convert_snake_to_camel
from app.domain.usecases import Usecase

class Product(BaseModel):
    id: int
    name: str
    portion: int
    portion_unity: str
    carbohidrates: float
    proteins: float
    fat: float
    saturated_fat: float

    class Config:
        alias_generator = convert_snake_to_camel
        allow_population_by_field_name = True

class GetProductsResponse(BaseModel):
    products: List[Product]

class GetProductsContract(Usecase):
    @abstractmethod
    def execute(self):
        raise NotImplementedError