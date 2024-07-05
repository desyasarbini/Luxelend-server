from app.models.base import Base
from sqlalchemy import String, Integer, DECIMAL
from sqlalchemy.orm import mapped_column
# from sqlalchemy.dialects.postgresql import ENUM

class Women(Base):
    __tablename__ = "women_product"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    category = mapped_column(String(255), nullable=False)
    product_name = mapped_column(String(255), nullable=False, unique=True)
    product_brand = mapped_column(String(255), nullable=False, unique=True)
    image_url = mapped_column(String(855), nullable=False)
    rent_price = mapped_column(DECIMAL(12,2), nullable=False)
    retail_price = mapped_column(DECIMAL(12,2), nullable=False)
    size = mapped_column(String(125), nullable=False)
    color = mapped_column(String(255), nullable=False)
    style = mapped_column(String(255), nullable=False)
    material = mapped_column(String(255), nullable=False)
    fit_note = mapped_column(String(255), nullable=False)

    def serialize(self, full=True):
        if full:
            return{
                'id': self.id,
                'category': self.category,
                'product_name': self.product_name,
                'product_brand': self.product_brand,
                'image_url': self.image_url,
                'rent_price': self.rent_price,
                'retail_price': self.retail_price,
                'size': self.size,
                'color': self.color,
                'style': self.style,
                'material': self.material,
                'fit_note': self.fit_note
            }
        else:
            return{
                'id': self.id,
                'category': self.category,
                'product_name': self.product_name,
                'product_brand': self.product_brand,
                'image_url': self.image_url,
                'rent_price': self.rent_price,
                'retail_price': self.retail_price
            }
    
    def __repr__(self):
        return f'<Women{self.id}>'