from app.models.base import Base
from sqlalchemy import String, Integer, Enum, DECIMAL
from sqlalchemy.orm import mapped_column

class Men(Base):
    __tablename__ = "men_product"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    category = mapped_column(Enum('t-shirts', 'pants', 'dress', 'Skirts', 'jacket', 'accesories', 'shoes'), nullable=False)
    product_name = mapped_column(String(40), nullable=False, unique=True)
    product_brand = mapped_column(String(40), nullable=False, unique=True)
    image_url = mapped_column(String(255), nullable=False)
    rent_price = mapped_column(DECIMAL(12,2), nullable=False)
    retail_price = mapped_column(DECIMAL(12,2), nullable=False)
    size = mapped_column(Enum('s','m','l','xl'), nullable=False)
    color = mapped_column(String(40), nullable=False, unique=True)
    style = mapped_column(String(155), nullable=False)
    material = mapped_column(String(155), nullable=False)
    fit_note = mapped_column(String(255), nullable=False)

