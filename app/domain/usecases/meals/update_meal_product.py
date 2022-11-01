from abc import abstractmethod
from pydantic import BaseModel
from app.domain.usecases import Usecase
from app.services.helpers.http import HttpResponse


class UpdateMealProductResponse(BaseModel):
    id: int
    portion: int

class UpdateMealProductParams(BaseModel):
    id: int
    portion: int

class UpdateMealProductContract(Usecase):
    @abstractmethod
    def execute(self, params: UpdateMealProductParams) -> HttpResponse[UpdateMealProductResponse]:
        raise NotImplementedError()
