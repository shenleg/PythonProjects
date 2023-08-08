from sqlalchemy import create_engine, text

from 第三方库.sqlalchemy.common import config

db_info = config.db_info["MySQL"]

url = db_info["sqlalchemy_url_format"].format(
    db_info["username"], db_info["password"], db_info["host"],
    db_info["port"], db_info["database"]
)

engine = create_engine(url, echo=False)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM student where id=1"))
    print("result type:", type(result))
    # print("result.all():", result.all())  # 游标完了就不可以获取数据

for row in result:
    print("row type:", type(row))
    print(row.id, row.name)  # 表字段
    print(row[0], row[1])  # 序号

