from sqlalchemy import Column, Integer, String, or_, select
from sqlalchemy.orm import declarative_base, relationship, mapped_column, Mapped

from 第三方库.sqlalchemy.common.database import UsingAlchemy

Base = declarative_base()


class Child(Base):
    # 定义表名
    __tablename__ = 'child'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(32))
    p_id: Mapped[int] = mapped_column(Integer)


class Parent(Base):
    # 定义表名
    __tablename__ = 'parent'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(32))


with UsingAlchemy() as ua:
    stmt = select(Parent, Child)
    print(stmt)
