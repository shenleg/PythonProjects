from sqlalchemy import text

from 第三方库.sqlalchemy.common.database import UsingAlchemy
from 第三方库.sqlalchemy.common.models import Student

with UsingAlchemy() as ua:
    # 在 filter 和 order_by 中使用
    query = ua.session.query(Student).filter(text("id=1")).order_by(text("id"))
    print(query)  # 打印查询对象能直接显示sql构造，也可以通过str(query)转换

    # 完整SQL
    query = ua.session.query(Student).from_statement(text("select * from Student where id = 1"))
    print(query)  # 打印查询对象能直接显示sql构造，也可以通过str(query)转换
    query = ua.session.query(text("id"), text("name")).from_statement(text("select id,name from Student where id = 1"))
    print(query)  # 打印查询对象能直接显示sql构造，也可以通过str(query)转换

