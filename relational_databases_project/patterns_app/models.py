from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


# SQLAlchemy model
class PatternType(Base):
    __tablename__ = "pattern_types"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    patterns = relationship("Pattern", back_populates="pattern_type")


class Pattern(Base):
    __tablename__ = "patterns"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text)
    pattern_type_id = Column(Integer, ForeignKey("pattern_types.id"))

    pattern_type = relationship("PatternType", back_populates="patterns")
    use_cases = relationship("UseCase", back_populates="pattern")


class UseCase(Base):
    __tablename__ = "use_cases"
    id = Column(Integer, primary_key=True)
    description = Column(Text)
    pattern_id = Column(Integer, ForeignKey("patterns.id"))

    pattern = relationship("Pattern", back_populates="use_cases")
