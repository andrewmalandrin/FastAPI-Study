from abc import abstractmethod
from pydantic import BaseModel
from typing import List
from app.services.helpers.string import convert_snake_to_camel

from app.domain.usecases import Usecase

class Product(BaseModel):
    id: int
    name: str
    portion: int
    carbohidrates: float
    proteins: float
    fat: float
    saturated_fat: float

    class Config:
        alias_generator = convert_snake_to_camel
        allow_population_by_field_name = True

class Meal(BaseModel):
    description: str
    products: List[Product]

class GetDietResponse(BaseModel):
    id: int
    meals: List[Meal]

class GetDietParams(BaseModel):
    id: int

class GetDietContract(Usecase):
    @abstractmethod
    def execute(self, diet_id: int):
        raise NotImplementedError()
