from abc import abstractmethod
from pydantic import BaseModel

from app.services.helpers.http import HttpResponse

from app.domain.usecases import Usecase


class UpdateDietResponse(BaseModel):
    id: int
    description: str

class UpdateDietParams(BaseModel):
    id: int
    description: str

class UpdateDietContract(Usecase):
    @abstractmethod
    def execute(self, params: UpdateDietParams) -> HttpResponse[UpdateDietResponse]:
        raise NotImplementedError()
