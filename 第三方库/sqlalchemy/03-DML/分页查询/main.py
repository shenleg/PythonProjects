from 第三方库.sqlalchemy.common.database import UsingAlchemy
from 第三方库.sqlalchemy.common.models import Student

page_current = 1
page_size = 2


with UsingAlchemy() as ua:
    query = ua.session.query(Student)
    print("all students:", query)

    offset = page_size * (page_current - 1)
    limit = page_size
    query = ua.session.query(Student).offset(offset).limit(limit)
    print("limit:", query)

    start = (page_current - 1) * page_size
    end = start + page_size
    query = ua.session.query(Student)[start:end]
    print("limit:", query)
