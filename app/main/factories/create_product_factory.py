from app.services.usecases.products import CreateProduct
from app.domain.usecases import Usecase
from app.infra.data.config import CSVFileManager
from app.infra.data.repositories.products import ProductsRepository

def create_product_factory() -> Usecase:
    file_manager_instance = CSVFileManager(
        'D:/users/pichau/devprojects/training/python/fastapi-study/app/infra/data/tsf/products.tsv'
    )
    return CreateProduct(
        products_repository=ProductsRepository(file_manager_instance=file_manager_instance)
    )
