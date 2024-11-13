from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Text
import base

class Size(Base):
    __tablename__ = "sizes"
    
    id = Column(Integer, primary_key=True, index=True)
    size = Column(String(10), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'))
    colors = relationship("SizeColor", backref="size")