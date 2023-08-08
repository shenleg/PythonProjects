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
# pip install pymysql
url = 'mysql+pymysql://shenle:f55fbb586bf5b9ab@mysql.sqlpub.com:3306/myshenle'
engine = create_engine(
    url,
    echo=True,  # echo 设为 True 会打印出实际执行的 sql，调试的时候更方便
    future=True,  # 使用 SQLAlchemy 2.0 API，向后兼容
    pool_size=5,  # 连接池的大小默认为 5 个，设置为 0 时表示连接无限制
    pool_recycle=3600,  # 设置时间以限制数据库自动断开
)

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
