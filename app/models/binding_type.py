from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime
)

from sqlalchemy.sql import func

from app.models.base import Base


class BindingType(Base):
    __tablename__ = "binding_types"

    id = Column(Integer, primary_key=True, index=True)

    binding_type_code = Column(
        String(30),
        unique=True,
        nullable=False,
        index=True
    )

    binding_type_name = Column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )

    display_order = Column(
        Integer,
        default=1,
        nullable=False
    )

    is_active = Column(
        Boolean,
        default=True,
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )
