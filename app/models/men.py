from app.models.base import Base
from sqlalchemy import String, Integer, Enum, DECIMAL, ARRAY
from sqlalchemy.orm import mapped_column

class Men(Base):
    __tablename__ = "men_product"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    category = mapped_column(Enum('t-shirts', 'pants', 'jacket', 'shoes', 'accessories', name='men_category'), nullable=False)
    product_name = mapped_column(String(255), nullable=False, unique=True)
    product_brand = mapped_column(String(255), nullable=False, unique=True)
    image_url = mapped_column(ARRAY(String(855)), nullable=False)
    rent_price = mapped_column(DECIMAL(12,2), nullable=False)
    retail_price = mapped_column(DECIMAL(12,2), nullable=False)
    size = mapped_column(ARRAY(String(125)), nullable=False)
    color = mapped_column(ARRAY(String(255)), nullable=False)
    style = mapped_column(ARRAY(String(255)), nullable=False)
    material = mapped_column(ARRAY(String(255)), nullable=False)
    fit_note = mapped_column(String(255), nullable=False)
    stock = mapped_column(Integer, nullable=False)

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
                'fit_note': self.fit_note,
                'stock': self.stock
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
        return f'<Men{self.id}>'