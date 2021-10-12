from app.interfaces.api_interfaces import ServiceInterface
from app.usecases.product_service import ProductService
from app.usecases.user_service import UserService

ProductService()
UserService()


def test_product_repository():
    assert issubclass(ProductService, ServiceInterface)


def test_user_repository():
    assert issubclass(UserService, ServiceInterface)
