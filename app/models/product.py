from app.models.base import Base
from sqlalchemy import String, Integer, DECIMAL, ForeignKey, DateTime, func
from sqlalchemy.orm import mapped_column, relationship

class Product(Base):
    __tablename__ = "product"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    category_id = mapped_column(Integer, ForeignKey("category.id", ondelete="CASCADE"))
    name = mapped_column(String(255), nullable=False)
    rented_price = mapped_column(DECIMAL(12,2), nullable=False)
    retail_price = mapped_column(DECIMAL(12,2), nullable=False)
    stock = mapped_column(Integer, nullable=False)
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at = mapped_column(DateTime(timezone=True), server_default=func.now())

    category_product = relationship("Category", back_populates="products")
    image_product = relationship("Product_image", back_populates="products")

    def serialize(self, full=True):
        if full:
            return{
                'id': self.id,
                'category_id': self.category_id,
                'name': self.name,
                'rented_price': self.rented_price,
                'retail_price': self.retail_price,
                'stock': self.stock
            }
        else:
            return{
                'id': self.id,
                'category_id': self.category_id,
                'name': self.name,
                'rented_price': self.rented_price,
                'retail_price': self.retail_price,
                'stock': self.stock,
                'created_at': self.created_at,
                'updated_at': self.updated_at
            }
    
    def __repr__(self):
        return f'<Product{self.id}>'
