from abc import abstractmethod
from pydantic import BaseModel
from app.domain.usecases import Usecase
from app.services.helpers.string import convert_snake_to_camel

class CreateUserResponse(BaseModel):
    id: int
    name: str
    weight: float
    carbo_kg: float
    fat_kg: float
    age: int

    class Config:
        alias_generator = convert_snake_to_camel
        allow_population_by_field_name = True

class CreateUserParams(BaseModel):
    name: str
    weight: float
    carbo_kg: float
    fat_kg: float
    age: int

    class Config:
        alias_generator = convert_snake_to_camel
        allow_population_by_field_name = True


class CreateUserCrontract(Usecase):
    @abstractmethod
    def execute(self, params: CreateUserParams):
        raise NotImplementedError