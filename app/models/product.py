from app.models.base import Base
from sqlalchemy import String, Integer, DECIMAL, ForeignKey, DateTime, func
from sqlalchemy.orm import mapped_column, relationship

class Product(Base):
    __tablename__ = "product"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    category_id = mapped_column(Integer, ForeignKey('category.id', ondelete="CASCADE"))
    gender_category_id = mapped_column(Integer, ForeignKey('gender_category.id', ondelete="CASCADE"))
    name = mapped_column(String(255), nullable=False)
    rented_price = mapped_column(DECIMAL(12,2), nullable=False)
    retail_price = mapped_column(DECIMAL(12,2), nullable=False)
    stock = mapped_column(Integer, nullable=False)
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    category = relationship("Category", back_populates="product")
    gender_category = relationship("Gender_category", back_populates="product")
    product_image = relationship("Product_image", back_populates="product")
    product_properties = relationship("Product_properties", back_populates="product")
    # transaction = relationship("Transaction", back_populates="product")

    def serialize(self, full=True):
        serialize_data = {
            'id': self.id,
            'category_id': self.category_id,
            'gender_category': self.gender_category_id,
            'name': self.name,
            'rented_price': self.rented_price,
            'retail_price': self.retail_price,
            'stock': self.stock
        }

        if full:
            serialize_data.update({
                'created_at': self.created_at,
                'updated_at': self.updated_at,
                'category': self.category.serialize() if self.category else None,
                'gender_category': self.gender_category.serialize() if self.gender_category else None,
                'product_images': [image.serialize() for image in self.product_image],
                'product_properties': [properties.serialize() for properties in self.product_properties],
                
            })

        return serialize_data
    
    def __repr__(self):
        return f'<Product{self.id}>'
