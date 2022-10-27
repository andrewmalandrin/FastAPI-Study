from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class UpdateDietFileParams:
    id: int
    description: str

@dataclass
class GetDietFileParams:
    id: int

@dataclass
class SaveDietFileParams:
    user_id: int
    description: str

class DietsRepositoryContract(ABC):
    @abstractmethod
    def get_diets(self):
        raise NotImplementedError()
    
    @abstractmethod
    def get_diet_by_filters(self, params: GetDietFileParams):
        raise NotImplementedError()

    @abstractmethod
    def create_diet(self, params: SaveDietFileParams):
        raise NotImplementedError()

    @abstractmethod
    def update_diet(self, params: UpdateDietFileParams):
        raise NotImplementedError()
