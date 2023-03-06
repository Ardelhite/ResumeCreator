from typing import Optional

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db_setting import DtoBase


class ItTechnologyMaster(DtoBase):
    """
    技術マスタ
    C, Docker, Vue.JS など
    """
    __tablename__ = 'it_tech_master'

    id: Mapped[str] = mapped_column(primary_key=True)
    jp_name: Mapped[Optional[str]]
    category: Mapped[list['ItTechnologyCategory']] = mapped_column(ForeignKey('it_tech_category_master.id'))


# 技術カテゴリマスタ (言語, FW, インフラ, 一般ITなど技術マスタに依存しない分野を含む)
class ItTechnologyCategory(DtoBase):
    """
    技術カテゴリマスタ
    言語, FW, インフラ, 一般ITなど技術マスタに依存しない分野を含む
    """
    __tablename__ = 'it_tech_category_master'

    id: Mapped[str] = mapped_column(primary_key=True)
    jp_name: Mapped[Optional[str]]



