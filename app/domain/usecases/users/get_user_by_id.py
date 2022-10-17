from abc import abstractmethod
from pydantic import BaseModel
from app.domain.usecases import Usecase
from app.services.helpers.string import convert_snake_to_camel


class GetUserByIdParams(BaseModel):
    id: int

class GetUserByIdResponse(BaseModel):
    id: int
    name: str
    weight: float
    carbo_kg: float
    fat_kg: float
    age: int

    class Config:
        alias_generator = convert_snake_to_camel
        allow_population_by_field_name = True


class GetUserByIdContract(Usecase):
    @abstractmethod
    def execute(self, params: GetUserByIdParams):
        raise NotImplementedError()
