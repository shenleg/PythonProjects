from sqlalchemy import create_engine, text

from 第三方库.sqlalchemy.common import config

db_info = config.db_info["MySQL"]

url = db_info["sqlalchemy_url_format"].format(
    db_info["username"], db_info["password"], db_info["host"],
    db_info["port"], db_info["database"]
)

engine = create_engine(url, echo=False)

# 使用 :var 传递
with engine.connect() as conn:
    result = conn.execute(
        text("SELECT * FROM student where id=:x"),
        {"x": 1}
    )

for row in result:
    print(row.id, row.name)  # 表字段


# 事先编译好参数
stmt = text("SELECT * FROM student where id=:x").bindparams(x=1)
