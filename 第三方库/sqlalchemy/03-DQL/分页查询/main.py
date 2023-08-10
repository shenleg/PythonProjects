from select import select

from 第三方库.sqlalchemy.common.database import UsingAlchemy
from 第三方库.sqlalchemy.common.models import Student

page_current = 1
page_size = 2


with UsingAlchemy() as ua:
    print("====1.x====")
    query = ua.session.query(Student)
    print("all students:", query)

    # 数据库原生
    offset = page_size * (page_current - 1)
    limit = page_size
    query = ua.session.query(Student).offset(offset).limit(limit)
    print("limit:", query)

    # 切片形式
    start = (page_current - 1) * page_size
    end = start + page_size
    query = ua.session.query(Student)[start:end]
    print("limit:", query)

    print("====2.x====")
    offset = page_size * (page_current - 1)
    limit = page_size
    stmt = select(Student)
    query = select(Student).offset(offset).limit(limit)
    print("limit:", query)
