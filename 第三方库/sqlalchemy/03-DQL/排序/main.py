from 第三方库.sqlalchemy.common.database import UsingAlchemy
from 第三方库.sqlalchemy.common.models import Student

page_current = 1
page_size = 2

with UsingAlchemy() as ua:
    query = ua.session.query(Student)
    print("all students:", query)

    query = ua.session.query(Student).order_by(Student.age, Student.t_id)
    print("order students:", query)

    # 拥有null值的行优先排在前面
    query = ua.session.query(Student).order_by(
        (Student.age.is_(None)+Student.t_id.is_(None)).desc(),
        Student.age, Student.t_id
    )
    print("order students:", query)
