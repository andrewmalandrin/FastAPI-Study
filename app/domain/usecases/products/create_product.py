from abc import abstractmethod
from pydantic import BaseModel, Field

from app.domain.usecases import Usecase

class CreateProductResponse(BaseModel):
    name: str
    portion: int
    portion_unity: str = Field(alias='portionUnity')
    carbo: float
    prot: float
    fat: float
    saturated_fat: float = Field(alias='saturatedFat')

    class Config:
        allow_population_by_field_name = True

class CreateProductParams(BaseModel):
    name: str
    portion: int
    portion_unity: str = Field(alias='portionUnity')
    carbo: float
    prot: float
    fat: float
    saturated_fat: float = Field(alias='saturatedFat')

    class Config:
        allow_population_by_field_name = True

class CreateProductContract(Usecase):
    @abstractmethod
    def execute(self, params: CreateProductParams):
        raise NotImplementedError
