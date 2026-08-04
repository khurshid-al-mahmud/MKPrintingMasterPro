"""
Database Base

Re-export the project's single SQLAlchemy Base.
"""

from app.models.base import Base

__all__ = ["Base"]