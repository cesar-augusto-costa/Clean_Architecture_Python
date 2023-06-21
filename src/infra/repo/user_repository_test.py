from faker import Faker

from .user_repository import UserRepository

faker = Faker()
user_repository = UserRepository()


def test_insert_user():
    """Should Insert User"""

    name = faker.name()
    password = faker.word()

    new_user = user_repository.insert_user(name, password)
    print(new_user)
