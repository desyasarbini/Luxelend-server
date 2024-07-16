from app.models.base import Base
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

class Gender_category(Base):
    __tablename__ = "gender_category"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    gender_id = mapped_column(Integer, ForeignKey('gender.id', ondelete="CASCADE"), primary_key=True)
    category_id = mapped_column(Integer, ForeignKey('category.id', ondelete="CASCADE"), primary_key=True)
    
    product = relationship("Product", back_populates="gender_category")
    gender = relationship("Gender", back_populates="gender_category")
    category = relationship("Category", back_populates="gender_category")

    def serialize(self):
        return{
            'id':self.id,
            'gender_id': self.gender_id,
            'category_id': self.category_id,
            'gender': self.gender.serialize() if self.gender else None,
            'category': self.category.serialize() if self.category else None
        }
    
    def __repr__(self):
        return f'<Gender_category{self.gender_id},{self.category_id}>'