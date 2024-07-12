from app.models.base import Base
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

class Product_image(Base):
    __tablename__ = "product_image"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    product_id = mapped_column(Integer, ForeignKey("product.id", ondelete="CASCADE"))
    value = mapped_column(String(255), nullable=False)

    products = relationship("Product", back_populates="image_product")

    def serialize(self):
        return{
            'id': self.id,
            'product_id': self.product_id,
            'value': self.value
        }
    
    def __repr__(self):
        return f'<Product_image{self.id}>'