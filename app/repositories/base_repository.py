"""
MKPrintingMasterPro ERP
Build-015

Base Repository

Purpose:
Provides reusable CRUD operations.

Status:
Production Ready
"""

from sqlalchemy.orm import Session


class BaseRepository:

    def __init__(self, db: Session, model):
        self.db = db
        self.model = model

    # -------------------------------------------------
    # Get By ID
    # -------------------------------------------------

    def get_by_id(self, object_id):

        return (
            self.db.query(self.model)
            .filter(self.model.id == object_id)
            .first()
        )

    # -------------------------------------------------
    # Get All
    # -------------------------------------------------

    def get_all(self):

        return (
            self.db.query(self.model)
            .all()
        )

    # -------------------------------------------------
    # Create
    # -------------------------------------------------

    def create(self, obj):

        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)

        return obj

    # -------------------------------------------------
    # Update
    # -------------------------------------------------

    def update(self, obj):

        self.db.commit()
        self.db.refresh(obj)

        return obj

    # -------------------------------------------------
    # Delete
    # -------------------------------------------------

    def delete(self, obj):

        self.db.delete(obj)
        self.db.commit()

    # -------------------------------------------------
    # Exists
    # -------------------------------------------------

    def exists(self, object_id):

        return (
            self.db.query(self.model)
            .filter(self.model.id == object_id)
            .first()
            is not None
        )

    # -------------------------------------------------
    # Count
    # -------------------------------------------------

    def count(self):

        return (
            self.db.query(self.model)
            .count()
        )