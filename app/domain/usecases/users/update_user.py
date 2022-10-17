from abc import abstractmethod
from pydantic import BaseModel
from typing import Optional
from app.domain.usecases import Usecase
from app.services.helpers.string import convert_snake_to_camel


class UpdateUserResponse(BaseModel):
    id: int
    name: str
    weight: float
    carbo_kg: float
    fat_kg: float
    age: int

class UpdateUserParams(BaseModel):
    id: int
    weight: Optional[float] = None
    carbo_kg: Optional[float] = None
    fat_kg: Optional[float] = None
    age: Optional[int] = None

class UpdateUserContract(Usecase):
    @abstractmethod
    def execute(self, params: UpdateUserParams):
        raise NotImplementedError()