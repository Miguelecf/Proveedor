from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Text
import base

class SizeColor(Base):
    __tablename__ = "size_colors"
    
    id = Column(Integer, primary_key=True, index=True)
    size_id = Column(Integer, ForeignKey('sizes.id'))
    color = Column(String(50), nullable=False)