from app.models.base import Base
from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, relationship

class Gender(Base):
    __tablename__ = "gender"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(25), nullable=False)

    gender_categories = relationship("Gender_category", back_populates="genders")

    def serialize(self):
        return{
            'id': self.id,
            'name': self.name
        }
    
    def __repr__(self):
        return f'<Gender{self.name}>'