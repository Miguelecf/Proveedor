from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Text
import base

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    unique_code = Column(String(10), unique=True, nullable=False)  # Código único del producto
    sizes = relationship("Size", backref="product")
    photo_urls = relationship("PhotoURL", backref="product")
