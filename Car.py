from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from db_cofig import Base


class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer(), primary_key=True)
    model = Column(String(25), nullable=False, unique=True)
    brand = Column(String(80), nullable=False, unique=True, index=True)  # https://docs.sqlalchemy.org/en/14/core/constraints.html#indexes
    year = Column(Integer())

    def __repr__(self):
        return f'\n<Car id={self.id} model={self.model} brand={self.brand} year={self.year}>'

    def __str__(self):
        return f'<Car id={self.id} model={self.model} brand={self.brand} year={self.year}>'
