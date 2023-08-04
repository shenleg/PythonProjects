from 第三方库.sqlalchemy.common.database import UsingAlchemy
from 第三方库.sqlalchemy.common.models import Student


with UsingAlchemy() as ua:
    student_list = ua.session.query(Student).all()
    print(student_list)

    # count
    student_total = ua.session.query(Student).count()
    print(student_total)

    # avg

    # max

    # min

