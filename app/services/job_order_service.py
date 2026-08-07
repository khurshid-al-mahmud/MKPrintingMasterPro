"""
MKPrintingMasterPro ERP

Job Order Service

Build-030
"""

from datetime import datetime

from app.models.job_order_master import JobOrderMaster
from app.models.job_order_item import JobOrderItem

from app.services.job_order_status_history_service import (
    JobOrderStatusHistoryService
)


class JobOrderService:
    """
    Job Order Service.
    """


    def __init__(
        self,
        job_order_repository,
        invoice_repository,
        numbering_service,
        db
    ):

        self.job_order_repository = job_order_repository

        self.invoice_repository = invoice_repository

        self.numbering_service = numbering_service

        self.status_history_service = (
            JobOrderStatusHistoryService(db)
        )



    # =====================================
    # Create Job Order from Invoice
    # =====================================

    def create_from_invoice(
        self,
        invoice_id: int,
    ):

        invoice = (
            self.invoice_repository.get_by_id(
                invoice_id
            )
        )


        if invoice is None:

            raise ValueError(
                "Invoice not found."
            )


        job_order_no = (
            self.numbering_service.generate_next_number(
                "JO"
            )
        )


        job_order = JobOrderMaster(

            job_order_no=job_order_no,

            job_order_date=datetime.now(),

            invoice_id=invoice.id,

            quotation_id=invoice.quotation_id,

            customer_id=invoice.customer_id,

            remarks=invoice.remarks,

            status="Open",

            priority="Normal",

        )


        for item in invoice.items:

            job_item = JobOrderItem(

                product_id=item.product_id,

                description=item.description,

                quantity=item.quantity,

                unit=item.unit,

                specification=item.specification,

                remarks=item.remarks,

            )


            job_order.items.append(
                job_item
            )


        job_order = (
            self.job_order_repository.create(
                job_order
            )
        )


        return job_order





    # =====================================
    # Get By ID
    # =====================================

    def get_by_id(
        self,
        job_order_id: int,
    ):

        return (
            self.job_order_repository.get_by_id(
                job_order_id
            )
        )





    # =====================================
    # Get All
    # =====================================

    def get_all(self):

        return (
            self.job_order_repository.get_all()
        )





    # =====================================
    # Update Job Order Status
    # Build-030 Phase-6 Step-3
    # =====================================

    def update_status(
        self,
        job_order_id: int,
        status: str,
        changed_by: str | None = "Admin",
        remarks: str | None = None
    ):


        job_order = (
            self.job_order_repository.get_by_id(
                job_order_id
            )
        )


        if job_order is None:

            raise ValueError(
                "Job Order not found."
            )



        allowed_status = [

            "Open",

            "Confirmed",

            "In Production",

            "Completed",

            "Delivered",

            "Cancelled",

        ]



        if status not in allowed_status:

            raise ValueError(
                "Invalid Job Order status."
            )



        # Previous Status

        old_status = str(
            job_order.status
        )



        # Prevent Duplicate History

        if old_status == status:

            raise ValueError(
                "Status is already same."
            )



        # Update Status

        job_order.status = status


        updated_job_order = (
            self.job_order_repository.update(
                job_order
            )
        )



        # =====================================
        # Save Status History
        # Fixed Build-030
        # =====================================

        final_changed_by = (
            changed_by
            if changed_by
            else "System"
        )


        self.status_history_service.create_history(

            job_order_id=job_order.id,

            old_status=old_status,

            new_status=status,

            changed_by=final_changed_by,

            remarks=remarks

        )



        return updated_job_order