from abc import abstractmethod
from pydantic import BaseModel
from app.domain.usecases import Usecase
from app.services.helpers.http import HttpResponse

class UpdateMealResponse(BaseModel):
    id: int
    description: str

class UpdateMealParams(BaseModel):
    id: int
    description: str

class UpdateMealContract(Usecase):
    @abstractmethod
    def execute(self, params: UpdateMealParams) -> HttpResponse[UpdateMealResponse]:
        raise NotImplementedError()
