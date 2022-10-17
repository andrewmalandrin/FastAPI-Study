from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class UsersData:
    id: int
    name: str
    weight: float
    carbo_kg: float
    fat_kg: float
    age: int

@dataclass
class SaveUserParams:
    id: int
    name: str
    weight: float
    carbo_kg: float
    fat_kg: float
    age: int

class UsersRepositoryContract(ABC):
    @abstractmethod
    def create_user(self, params: SaveUserParams):
        raise NotImplementedError()

    @abstractmethod
    def get_users(self):
        raise NotImplementedError()

    @abstractmethod
    def get_user_by_filters(self, id: int):
        raise NotImplementedError()
