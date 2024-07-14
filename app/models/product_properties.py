from app.models.base import Base
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

class Product_properties(Base):
    __tablename__ = "product_properties"

    product_id = mapped_column(Integer, ForeignKey('product.id', ondelete="CASCADE"), primary_key=True)
    property_id = mapped_column(Integer, ForeignKey('property.id', ondelete="CASCADE"), primary_key=True)

    product = relationship("Product", back_populates="product_properties")
    property = relationship("Property", back_populates="product_properties")

    def serialize(self):
        return{
            'product_id': self.product_id,
            'property_id': self.property_id
        }
    
    def __repr__(self):
        return f'<Product_properties{self.product_id},{self.property_id}>'