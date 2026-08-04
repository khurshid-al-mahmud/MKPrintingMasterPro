"""
MKPrintingMasterPro ERP
Build-016

Template Field Mapping Repository

Purpose:
Repository for TemplateFieldMapping CRUD operations.

Status:
Production Ready
"""

from sqlalchemy.orm import Session

from app.models.template_field_mapping import (
    TemplateFieldMapping,
)

from app.repositories.base_repository import BaseRepository


class TemplateFieldMappingRepository(BaseRepository):
    """
    Template Field Mapping Repository
    """


    def __init__(
        self,
        db: Session,
    ):

        super().__init__(
            db,
            TemplateFieldMapping
        )


    # =====================================
    # GET ALL ACTIVE MAPPINGS
    # =====================================

    def get_all_active(self):

        return (
            self.db.query(
                TemplateFieldMapping
            )
            .filter(
                TemplateFieldMapping.is_active.is_(True)
            )
            .order_by(
                TemplateFieldMapping.display_order
            )
            .all()
        )


    # =====================================
    # GET BY ID
    # =====================================

    def get_by_id(
        self,
        mapping_id: int,
    ):

        return (
            self.db.query(
                TemplateFieldMapping
            )
            .filter(
                TemplateFieldMapping.id == mapping_id
            )
            .first()
        )


    # =====================================
    # GET BY TEMPLATE
    # =====================================

    def get_by_template(
        self,
        template_id: int,
    ):

        return (
            self.db.query(
                TemplateFieldMapping
            )
            .filter(
                TemplateFieldMapping.template_id == template_id,
                TemplateFieldMapping.is_active.is_(True)
            )
            .order_by(
                TemplateFieldMapping.display_order
            )
            .all()
        )


    # =====================================
    # CREATE
    # =====================================

    def create_mapping(
        self,
        mapping: TemplateFieldMapping,
    ):

        self.db.add(mapping)

        self.db.commit()

        self.db.refresh(mapping)

        return mapping



    # =====================================
    # UPDATE
    # =====================================

    def update_mapping(
        self,
    ):

        self.db.commit()



    # =====================================
    # SOFT DELETE
    # =====================================

    def delete_mapping(
        self,
        mapping: TemplateFieldMapping,
    ):

        setattr(
            mapping,
            "is_active",
            False,
        )

        self.db.commit()

        self.db.refresh(mapping)

        return True