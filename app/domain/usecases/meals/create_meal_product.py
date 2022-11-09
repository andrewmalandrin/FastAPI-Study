from abc import abstractmethod
from pydantic import BaseModel

from app.domain.usecases import Usecase
from app.services.helpers.http import HttpResponse
from app.services.helpers.string import convert_snake_to_camel


class CreateMealProductResponse(BaseModel):
    id: int
    meal_id: int
    product_id: int
    product_name: str
    portion: int

    class Config:

        alias_generator = convert_snake_to_camel
        allow_population_by_field_name = True

class CreateMealProductParams(BaseModel):
    meal_id: int
    product_id: int
    portion: int

    class Config:

        alias_generator = convert_snake_to_camel
        allow_population_by_field_name = True

class CreateMealProductContract(Usecase):
    @abstractmethod
    def execute(self, params: CreateMealProductParams) -> HttpResponse[CreateMealProductResponse]:
        raise NotImplementedError()
