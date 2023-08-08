from sqlalchemy import func

from 第三方库.sqlalchemy.common.database import UsingAlchemy
from 第三方库.sqlalchemy.common.models import Student


with UsingAlchemy() as ua:
    # count
    student_total = ua.session.query(Student).count()
    print(student_total)
    student_total = ua.session.query(func.count("*")).select_from(Student).scalar()
    print(student_total)
    student_total = ua.session.query(func.count(Student.id)).scalar()  # 确定是主键，可以省略select_from
    print(student_total)

    # avg

    # max

    # min

