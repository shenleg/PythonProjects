from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


# 0.定义ORM数据库表映射类，所有操作基于此类
class Student(Base):
    # 定义表名
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    age = Column(Integer)


# 1.创建连接
# echo参数为True时，会显示每条执行的SQL语句
url = 'mysql+pymysql://shenle:f55fbb586bf5b9ab@mysql.sqlpub.com:3306/myshenle'
engine = create_engine(url, echo=True)

# 2.创建会话
Session = sessionmaker(bind=engine)
session = Session()

# 3.执行语句
s = Student(name="name", age=19)
session.add(s)

# 4.提交
session.commit()

# 5.关闭
session.close()

# 回滚
# session.rollback()

"""
官方文档：https://docs.sqlalchemy.org/en/20/
"""
