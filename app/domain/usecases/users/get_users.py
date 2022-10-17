from abc import abstractmethod
from pydantic import BaseModel
from typing import List
from app.domain.usecases import Usecase
from app.services.helpers.string import convert_snake_to_camel


class User(BaseModel):
    id: int
    name: str
    weight: float
    carbo_kg: float
    fat_kg: float
    age: int

    class Config:
        alias_generator = convert_snake_to_camel
        allow_population_by_field_name = True


class GetUsersResponse(BaseModel):
    users: List[User]


class GetUsersContract(Usecase):
    @abstractmethod
    def execute(self):
        raise NotImplementedError()
