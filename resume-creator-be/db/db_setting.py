from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, DeclarativeBase

db_user_name = 'local_tset_admin'
db_user_pw = 'local_test_pw'
host = 'localhost'
port = 5432
db_name = 'resume_creator'
char_set = 'utf-8'

engine = create_engine(f'postgresql+psycopg2://{db_user_name}:{db_user_pw}@{host}:{port}/{db_name}', echo=True)


class DtoBase(DeclarativeBase):

    def init_master(self):
        pass


class DtoCrudFacade:
    @staticmethod
    def insert_records(new_records: List[DtoBase]):
        with Session(engine) as db_session:
            db_session.add_all(new_records)

    @staticmethod
    def get_records(key_records: List[DtoBase]) -> List[DtoBase]:
        for key_record in key_records:
            print(key_record.__dict__)


if __name__ == '__main__':
    """
    ローカルテスト
    psql -d resume_creator -U local_tset_admin -h localhost:5432
    """
    from db.dao.master.certificate_master import CertificateCategoryMaster

    test_category = CertificateCategoryMaster(
        id='test_it_certification',
        jp_name='テストIT資格'
    )
    DtoCrudFacade.insert_records([test_category])

    DtoCrudFacade.get_records([CertificateCategoryMaster(
        id='test_it_certification'
    )])

