from db.db_setting import DtoBase

from sqlalchemy.orm import Mapped, mapped_column


# 学位マスタ
class DegreeMaster(DtoBase):
    __tablename__ = 'degree_master'

    id: Mapped[str] = mapped_column(primary_key=True)

