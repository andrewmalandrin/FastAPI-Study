from abc import abstractmethod
from pydantic import BaseModel

from app.domain.usecases import Usecase
from app.services.helpers.http import HttpResponse

class DeleteProductResponse(BaseModel):
    id: int
    name: str

class DeleteProductParams(BaseModel):
    id: int

class DeleteProductContract(Usecase):
    @abstractmethod
    def execute(self, params: DeleteProductParams) -> HttpResponse:
        raise NotImplementedError()