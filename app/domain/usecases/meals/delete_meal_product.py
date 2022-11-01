from abc import abstractmethod
from pydantic import BaseModel
from app.domain.usecases import Usecase
from app.services.helpers.http import HttpResponse

class DeleteMealProductResponse(BaseModel):
    message: str

class DeleteMealProductParams(BaseModel):
    id: int

class DeleteMealProductContract(Usecase):
    @abstractmethod
    def execute(self, params: DeleteMealProductParams) -> HttpResponse[DeleteMealProductResponse]:
        raise NotImplementedError()
