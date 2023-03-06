from fastapi import FastAPI
from db.db_setting import DtoBase, engine
from db.dao.master.it_technology_master import ItTechnologyMaster, ItTechnologyCategory
from db.dao.master.certificate_master import (
    CertificateMaster,
    ReplacedCertificateMaster,
    CertificateCategoryMaster,
    CertificateCategoryRelationMaster
)

# DBテーブルの作成と確認
ItTechnologyMaster.metadata.create_all(bind=engine)
ItTechnologyCategory.metadata.create_all(bind=engine)
CertificateMaster.metadata.create_all(bind=engine)
ReplacedCertificateMaster.metadata.create_all(bind=engine)
CertificateCategoryMaster.metadata.create_all(bind=engine)
CertificateCategoryRelationMaster.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
async def test():
    return {'mes': 'test'}

