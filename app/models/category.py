from app.models.base import Base
from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, relationship

class Category(Base):
    __tablename__ = "category"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(255))

    product = relationship("Product", back_populates="category")
    # gender_category = relationship("Gender_category", back_populates="category")

    def serialize(self):
        return{
            'id': self.id,
            'name': self.name
        }
    
    def __repr__(self):
        return f'<Category{self.id} - {self.name}>'