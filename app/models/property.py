from app.models.base import Base
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

class Property(Base):
    __tablename__ = "property"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    property_category_id = mapped_column(Integer, ForeignKey('property_category.id', ondelete="CASCADE"))
    value = mapped_column(String(225), nullable=False)

    category_property = relationship("Property_category", back_populates="")