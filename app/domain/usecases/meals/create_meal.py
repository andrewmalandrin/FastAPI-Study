from abc import abstractmethod
from pydantic import BaseModel
from typing import List, Optional
from app.domain.usecases import Usecase
from app.services.helpers.string import convert_snake_to_camel
from app.services.helpers.http import HttpResponse


class ProductParams(BaseModel):
    product_id: int
    portion: int
    name: Optional[str] = None

    class Config:
        alias_generator = convert_snake_to_camel
        allow_population_by_field_name = True

class CreateMealResponse(BaseModel):
    id: int
    diet_id: int
    products: List[ProductParams]

class CreateMealParams(BaseModel):
    diet_id: int
    description: str
    products: List[ProductParams]

    class Config:
        alias_generator = convert_snake_to_camel
        allow_population_by_field_name = True

class CreateMealContract(Usecase):
    @abstractmethod
    def execute(self, params: CreateMealParams) -> HttpResponse[CreateMealResponse]:
        raise NotImplementedError()
