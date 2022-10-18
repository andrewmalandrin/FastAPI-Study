from abc import abstractmethod
from pydantic import BaseModel
from typing import Optional

from app.domain.usecases import Usecase
from app.services.contracts.products_repository_contract import UpdateProductParams
from app.services.helpers.http import HttpResponse
from app.services.helpers.string import convert_snake_to_camel


class UpdateProductResponse(BaseModel):
    id: int
    name: str
    portion: int
    portion_unity: str
    carbo: float
    prot: float
    fat: float
    saturated_fat: float
    
    class Config:
        alias_generator = convert_snake_to_camel
        allow_population_by_field_name = True

class UpdateProductParams(BaseModel):
    id: int
    name: Optional[str] = None
    portion: Optional[int] = None
    portion_unity: Optional[str] = None
    carbo: Optional[float] = None
    prot: Optional[float] = None
    fat: Optional[float] = None
    saturated_fat: Optional[float] = None

    class Config:
        alias_generator = convert_snake_to_camel
        allow_population_by_field_name = True

class UpdateProductContract(Usecase):
    @abstractmethod
    def execute(self, params: UpdateProductParams) -> HttpResponse[UpdateProductResponse]:
        raise NotImplementedError()
