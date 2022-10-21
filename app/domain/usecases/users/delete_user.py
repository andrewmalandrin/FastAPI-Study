from abc import abstractmethod
from pydantic import BaseModel
from app.domain.usecases import Usecase


class DeleteUserResponse(BaseModel):
    id: int
    name: str

class DeleteUserParams(BaseModel):
    id: int

class DeleteUserContract(Usecase):
    @abstractmethod
    def execute(self, params: DeleteUserParams):
        raise NotImplementedError
