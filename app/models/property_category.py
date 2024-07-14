from app.models.base import Base
from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, relationship

class Property_category(Base):
    __tablename__ = "property_category"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(255))

    property = relationship("Property", back_populates="property_category")

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
    
    def __repr__(self):
        return f'<Property_category{self.name}>'