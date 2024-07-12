from app.models.base import Base
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

class Gender_category(Base):
    __tablename__ = "gender_category"

    gender_id = mapped_column(Integer, ForeignKey('gender.id', ondelete="CASCADE"))
    category_id = mapped_column(Integer, ForeignKey('category.id', ondelete="CASCADE"))

    genders = relationship("Gender", back_populates="gender_categories")
    categories = relationship("Category", back_populates="gender_categories")

    def serialize(self):
        return{
            'gender_id': self.gender_id,
            'category_id': self.category_id
        }
    
    def __repr__(self):
        return f'<Gender_category{self.gender_id},{self.category_id}>'