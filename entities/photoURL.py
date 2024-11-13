from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Text
import base

class PhotoURL(Base):
    __tablename__ = "photo_urls"
    
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(255), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'))