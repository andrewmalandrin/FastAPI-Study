from app.domain.usecases import Usecase
from abc import abstractmethod
from pydantic import BaseModel, Field
from typing import Optional


class GetProductResponse(BaseModel):
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


class GetProductParams(BaseModel):
    id: int
    portion: Optional[int] = None

class GetProductContract(Usecase):
    @abstractmethod
    def execute(self, params: GetProductParams):
        raise NotImplementedError()
