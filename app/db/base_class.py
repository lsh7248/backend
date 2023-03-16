"""
DB에서 사용할 기본 Class 선언
"""
import re
from datetime import datetime

from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import as_declarative, declared_attr

# Base = declarative_base()


@as_declarative()
class Base:
    id: int = Column(Integer, primary_key=True, index=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    @declared_attr
    def __table__(cls) -> str:
        return re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__name__).lower()
