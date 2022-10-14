from abc import ABC, abstractmethod
from typing import Any, Optional

from app.services.helpers.http import HttpResponse

class Usecase(ABC):
    @abstractmethod
    def execute(self, *args: Optional[Any]) -> HttpResponse:
        raise NotImplementedError('This method must be implemented')
