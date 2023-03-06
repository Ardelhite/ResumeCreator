from typing import Optional
from datetime import datetime

from sqlalchemy import String, ForeignKey, DATETIME
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db_setting import DtoBase


class CertificateMaster(DtoBase):
    """資格マスタ"""
    __tablename__ = 'certificate_master'

    id: Mapped[str] = mapped_column(primary_key=True)
    jp_name: Mapped[Optional[str]]
    # category: Mapped[str] = relationship(ForeignKey('certificate_category_master.id'))


class ReplacedCertificateMaster(DtoBase):
    """名前が変更になった資格のマスタ"""
    __tablename__ = 'replaced_certificate_master'

    id: Mapped[str] = mapped_column(primary_key=True)
    jp_name: Mapped[Optional[str]]
    replaced_certificate: Mapped[str] = mapped_column(ForeignKey('certificate_master.id'))
    replaced_at: Mapped[datetime]


class CertificateCategoryMaster(DtoBase):
    """資格カテゴリマスタ"""
    __tablename__ = 'certificate_category_master'

    id: Mapped[str] = mapped_column(primary_key=True)
    jp_name: Mapped[Optional[str]]


class CertificateCategoryRelationMaster(DtoBase):
    """資格カテゴリと技術のマッピングテーブル"""
    __tablename__ = 'certificate_category_relation_master'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cert_category: Mapped[str] = mapped_column(ForeignKey('certificate_category_master.id'))
    tech_type: Mapped[Optional[str]] = mapped_column(ForeignKey('it_tech_master.id'))
    # DBスペシャリストなど特定の製品等に依存しない資格の場合
    other_tech_category: Mapped[Optional[str]] = mapped_column(ForeignKey('it_tech_category_master.id'))

