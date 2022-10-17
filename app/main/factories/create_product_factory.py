from app.services.usecases.products import CreateProduct
from app.domain.usecases import Usecase
from app.infra.data.config import CSVFileManager
from app.infra.data.repositories.products import ProductsRepository
from app.services.enums import PathsEnum

def create_product_factory() -> Usecase:
    file_manager_instance = CSVFileManager(
        PathsEnum.PRODUCTS_PATH
    )
    return CreateProduct(
        products_repository=ProductsRepository(file_manager_instance=file_manager_instance)
    )
