from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

@dataclass
class UsersData:
    id: int
    name: str
    weight: float
    carbo_kg: float
    fat_kg: float
    age: int

@dataclass
class UpdateFileUserParams:
    id: int
    weight: Optional[float] = None
    carbo_kg: Optional[float] = None
    fat_kg: Optional[float] = None
    age: Optional[int] = None

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
    
    @abstractmethod
    def update_user(self, params: UpdateFileUserParams):
        raise NotImplementedError()

    @abstractmethod
    def delete_user(self, id: int):
        raise NotImplementedError()
