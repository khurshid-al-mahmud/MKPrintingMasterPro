"""
MKPrintingMasterPro ERP

Production Output Service

Build-034
"""

from sqlalchemy.orm import Session

from app.repositories.production_output_repository import (
    ProductionOutputRepository,
)

from app.schemas.production_output import (
    ProductionOutputCreate,
    ProductionOutputUpdate,
)


class ProductionOutputService:
    """
    Service layer for Production Output.
    """

    def __init__(self):
        self.repository = ProductionOutputRepository()


    def create_output(
        self,
        db: Session,
        data: ProductionOutputCreate,
    ):

        return self.repository.create(
            db,
            data,
        )


    def get_output(
        self,
        db: Session,
        output_id: int,
    ):

        return self.repository.get_by_id(
            db,
            output_id,
        )


    def get_outputs(
        self,
        db: Session,
    ):

        return self.repository.get_all(
            db,
        )


    def update_output(
        self,
        db: Session,
        output_id: int,
        data: ProductionOutputUpdate,
    ):

        production_output = (
            self.repository.get_by_id(
                db,
                output_id,
            )
        )

        if not production_output:
            return None

        return self.repository.update(
            db,
            production_output,
            data,
        )


    def delete_output(
        self,
        db: Session,
        output_id: int,
    ):

        production_output = (
            self.repository.get_by_id(
                db,
                output_id,
            )
        )

        if not production_output:
            return False

        self.repository.delete(
            db,
            production_output,
        )

        return True