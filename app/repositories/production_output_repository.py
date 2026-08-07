"""
MKPrintingMasterPro ERP

Production Output Repository

Build-034
"""

from sqlalchemy.orm import Session

from app.models.production_output import ProductionOutput
from app.schemas.production_output import ProductionOutputCreate
from app.schemas.production_output import ProductionOutputUpdate


class ProductionOutputRepository:
    """
    Repository for Production Output operations.
    """

    def create(
        self,
        db: Session,
        data: ProductionOutputCreate,
    ) -> ProductionOutput:

        production_output = ProductionOutput(
            **data.model_dump()
        )

        db.add(production_output)
        db.commit()
        db.refresh(production_output)

        return production_output


    def get_by_id(
        self,
        db: Session,
        output_id: int,
    ) -> ProductionOutput | None:

        return (
            db.query(ProductionOutput)
            .filter(
                ProductionOutput.id == output_id
            )
            .first()
        )


    def get_all(
        self,
        db: Session,
    ) -> list[ProductionOutput]:

        return (
            db.query(ProductionOutput)
            .order_by(
                ProductionOutput.id.desc()
            )
            .all()
        )


    def update(
        self,
        db: Session,
        production_output: ProductionOutput,
        data: ProductionOutputUpdate,
    ) -> ProductionOutput:

        update_data = data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(
                production_output,
                field,
                value
            )

        db.commit()
        db.refresh(production_output)

        return production_output


    def delete(
        self,
        db: Session,
        production_output: ProductionOutput,
    ) -> None:

        db.delete(production_output)
        db.commit()