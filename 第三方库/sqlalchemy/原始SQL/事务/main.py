from sqlalchemy import create_engine, text

from 第三方库.sqlalchemy.common import config

db_info = config.db_info["MySQL"]

url = db_info["sqlalchemy_url_format"].format(
    db_info["username"], db_info["password"], db_info["host"],
    db_info["port"], db_info["database"]
)

engine = create_engine(url, echo=False)

# 手动commit
with engine.connect() as conn:
    conn.execute(
        text("INSERT INTO student(name, age) values(:x, :y)"),
        [
            {"x": "test1", "y": "55"},
            {"x": "test2", "y": "55"},
        ]
    )
    conn.commit()

# 半自动commit
with engine.begin() as conn:
    conn.execute(
        text("INSERT INTO student(name, age) values(:x, :y)"),
        [
            {"x": "test1", "y": "55"},
            {"x": "test2", "y": "55"},
        ]
    )
