from 第三方库.sqlalchemy.common.database import UsingAlchemy
from 第三方库.sqlalchemy.common.models import Student

page_current = 1
page_size = 2
offset = page_size * (page_current - 1)
limit = page_size

with UsingAlchemy() as ua:
    query = ua.session.query(Student)
    print("all students:", query)

    query = ua.session.query(Student).offset(offset).limit(limit)
    print("limit:", query)

    query = ua.session.query(Student)[1:2]
    print("limit:", query)
