"""
Database Dependency.

Reusable database dependency
for the entire ERP system.
"""

from typing import Generator

from sqlalchemy.orm import Session

from app.database.engine import SessionLocal


def get_db() -> Generator[Session, None, None]:
    """
    Provide database session.
    """

    db: Session = SessionLocal()

    try:
        yield db

    finally:
        db.close()







# Future shared database dependencies
# for authentication, transactions,
# and request-scoped services
# will be added here.