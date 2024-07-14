from app.models.base import Base
from sqlalchemy import Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import mapped_column, relationship

class Transaction(Base):
    __tablename__ = "transaction"

    user_id = mapped_column(Integer, ForeignKey('user.id', ondelete="CASCADE"), primary_key=True)
    product_id = mapped_column(Integer, ForeignKey('product.id', ondelete="CASCADE"), primary_key=True)
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())

    # users = relationship("Users", back_populates="transaction")
    # product = relationship("Product", back_populates="transaction")

    def serialize(self, full=True):
        if full:
            return{
                'user_id': self.user_id,
                'product_id': self.product_id
            }
        else:
            return{
                'user_id': self.user_id,
                'product_id': self.product_id,
                'created_at': self.created_at
            }
    
    def __repr__(self):
        return f'<Transaction{self.user_id},{self.product_id}>'