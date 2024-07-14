from app.models.base import Base
from sqlalchemy import String, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import mapped_column, relationship
import bcrypt

class Users(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    username = mapped_column(String(255), nullable=False)
    password = mapped_column(String(255), nullable=False)
    phone_number = mapped_column(String(255), nullable=False)
    gender_id = mapped_column(ForeignKey('gender.id', ondelete="CASCADE"))
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())

    # gender = relationship("Gender", back_populates="users")
    # transaction = relationship("Transaction", back_populates="users")

    def serialize(self, full=True):
        if full:
            return{
                'id': self.id,
                'username': self.username,
                'phone_number': self.phone_number,
                'gender_id': self.gender_id
            }
        else:
            return{
                'id': self.id,
                'username': self.username,
                'phone_number': self.phone_number,
                'gender_id': self.gender_id,
                'created_at': self.created_at
            }
    
    def __repr__(self):
        return f'<Users{self.username}>'

    def create_password(self, password):
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
