from sqlalchemy import Column, Integer, String, JSON, DATETIME, FetchedValue, \
    create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class ResolveParams(Base):
    __tablename__ = 'resolve_params'
    resolve_params_id = Column(Integer, primary_key=True, autoincrement=True)
    schema_id = Column(Integer)
    resolve_params_content = Column(JSON)
    custom_model_params_content = Column(JSON)
    characteristic_check = Column(JSON)
    comment = Column(String(512))
    created_by = Column(String(32))
    created_time = Column(DATETIME, server_default=FetchedValue())
    updated_by = Column(String(32))
    updated_time = Column(DATETIME, server_default=FetchedValue())


if __name__ == '__main__':
    url = 'mysql+pymysql://{}:{}@{}:{}/{}'.format("test", "test", "10.101.4.31",
                                                  "3306", "zhang")
    engine = create_engine(url, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(ResolveParams).all()
    for s in res:
        print(s.schematic_name)

    session.commit()
    session.close()
