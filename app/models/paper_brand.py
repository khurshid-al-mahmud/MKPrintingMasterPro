from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import BaseModel


class PaperBrand(BaseModel):
    __tablename__ = "paper_brands"

    paper_brand_code: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        index=True,
        nullable=False,
    )

    paper_brand_name: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        index=True,
        nullable=False,
    )

    display_order: Mapped[int] = mapped_column(
        default=1,
        nullable=False,
    )
