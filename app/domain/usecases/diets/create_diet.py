from abc import abstractmethod
from pydantic import BaseModel
from typing import List, Optional
from app.services.helpers.string import convert_snake_to_camel

from app.domain.usecases import Usecase

class Products(BaseModel):
    product_id: int
    portion: int
    name: Optional[str] = None

    class Config:
        alias_generator = convert_snake_to_camel
        allow_population_by_field_name = True


class Meals(BaseModel):
    description: str
    products: List[Products]

class CreateDietResponse(BaseModel):
    diet_id: int
    user_id: int
    user_name: str
    meals: List[Meals]

    class Config:
        alias_generator = convert_snake_to_camel
        allow_population_by_field_name = True


class CreateDietParams(BaseModel):
    user_id: int
    description: str
    meals: List[Meals]

    class Config:
        alias_generator = convert_snake_to_camel
        allow_population_by_field_name = True

class CreateDietContract(Usecase):
    @abstractmethod
    def execute(self, params: CreateDietParams):
        raise NotImplementedError()
