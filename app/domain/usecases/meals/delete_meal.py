from abc import abstractmethod
from pydantic import BaseModel
from app.domain.usecases import Usecase
from app.services.helpers.http import HttpResponse


class DeleteMealParams(BaseModel):
    id: int

class DeleteMealContract(Usecase):
    @abstractmethod
    def execute(self, params) -> HttpResponse:
        raise NotImplementedError()
