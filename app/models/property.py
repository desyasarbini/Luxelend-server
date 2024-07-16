from app.models.base import Base
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

class Property(Base):
    __tablename__ = "property"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    property_category_id = mapped_column(Integer, ForeignKey('property_category.id', ondelete="CASCADE"))
    value = mapped_column(String(225), nullable=False)

    property_category = relationship("Property_category", back_populates="property")
    product_properties = relationship("Product_properties", back_populates="property")

    def serialize(self, include_category=False):
        serialize_data = {
            'id': self.id,
            'property_category_id': self.property_category_id,
            'value': self.value,
        }

        if include_category:
            serialize_data['property_category'] = self.property_category.serialize() if self.property_category else None
        
        return serialize_data

    
    def __repr__(self):
        return f'<Property{self.id}>'