import enum

from sqlalchemy import Column, Enum, ForeignKey, Integer, String

from src.infra.config import Base


class AnimalTypes(enum.Enum):
    """Defining Anymals Types"""

    dog = "dog"
    cat = "cat"
    fish = "fish"
    turtle = "turtle"


class Pets(Base):
    """Pets Entity"""

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    spacie = Column(Enum(AnimalTypes), nullable=False)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"Pet: [name={self.name}, specie={self.spacie}, user_id={self.user_id}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.name == other.name
            and self.spacie == other.spacie
            and self.age == other.age
            and self.user_id == other.user_id
        ):
            return True
        return False
