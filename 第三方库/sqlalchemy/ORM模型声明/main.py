from datetime import datetime
from typing import Optional

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship

from 第三方库.sqlalchemy.common.database import UsingAlchemy


class Base(DeclarativeBase):
    pass

"""
1.无论定义什么类型，只要类字段名和数据库字段名对应上，那么都能从数据库中获取到数据，类型为数据库类型
2.String长度对获取数据无影响
"""

class User(Base):
    __tablename__ = "users"  # 指定表名

    # 使用 Mapped 相关联 Python 数据类型
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    # 可在 mapped_column 指定更具体的类型
    name: Mapped[str] = mapped_column(String(1))
    # Optional[str] 为可选类型，自动适配数据库类型
    fullname: Mapped[Optional[str]]

    # birthday: Mapped[datetime]

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


with UsingAlchemy() as ua:
    users = ua.session.query(User).all()
    print(users)
    print(type(users[0].id))
