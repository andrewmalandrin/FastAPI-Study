from pydantic import BaseModel


class Product_Base(BaseModel):
    name: str
    portion: int
    carbohidrates: float
    proteins: float
    fat: float
    saturated_fat: float