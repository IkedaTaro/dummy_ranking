from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Goal(Base):
    __tablename__ = 'goal'
    id = Column(Integer, primary_key=True)
    description = Column(String(100), nullable=False)

class Score(Base):
    __tablename__ = 'score'
    id = Column(Integer, primary_key=True)
    value = Column(Integer, nullable=False)
    goal_id = Column(Integer, ForeignKey('goal.id'), nullable=False)
    goal = relationship("Goal", back_populates="scores")
    
Goal.scores = relationship("Score", order_by=Score.id, back_populates="goal")
