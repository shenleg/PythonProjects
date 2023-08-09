from 第三方库.sqlalchemy.common.database import UsingAlchemy
from 第三方库.sqlalchemy.common.models import Student

with UsingAlchemy() as ua:
    # like / not like
    query = ua.session.query(Student).filter(
        Student.name.like("%张三_")
    )
    print("like:", query)
    query = ua.session.query(Student).filter(
        Student.name.not_like("%张三_")
    )
    print("not like:", query)

    # is / is not
    query = ua.session.query(Student).filter(
        Student.name.is_(None)
    )
    print("is:", query)
    query = ua.session.query(Student).filter(
        Student.name == None
    )
    print("is:", query)
    query = ua.session.query(Student).filter(
        Student.name.is_not(None)
    )
    print("is not:", query)

    # in / not in
    query = ua.session.query(Student).filter(
        Student.id.in_([1, 2])
    )
    print("in:", query)
    query = ua.session.query(Student).filter(
        Student.id.not_in([1, 2])
    )
    print("not in:", query)
    query = ua.session.query(Student).filter(
        Student.id.in_(ua.session.query(Student.id).filter(Student.id == 1))
    )
    print("in:", query)

    # exist / not exist
    res = ua.session.query(Student).filter(Student.id == 1)
    query = ua.session.query(res.exists())
    print("exists:", query)

    # between
    query = ua.session.query(Student).filter(
        Student.id.between(1, 3)
    )
    print("between:", query)
