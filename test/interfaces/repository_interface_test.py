from app.interfaces.api_interfaces import RepositoryInterface
from app.repositories.product_repository import ProductRepository
from app.repositories.user_repository import UserRepository

ProductRepository()
UserRepository()


def test_product_repository():
    assert issubclass(ProductRepository, RepositoryInterface)


def test_user_repository():
    assert issubclass(UserRepository, RepositoryInterface)
