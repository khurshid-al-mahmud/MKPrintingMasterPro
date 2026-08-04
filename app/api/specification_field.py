"""
Specification Field API.

REST API endpoints
for Dynamic Specification Field Management.
"""

import traceback

from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies.service import (
    get_specification_field_service,
)

from app.schemas.specification_field import (
    SpecificationFieldCreate,
    SpecificationFieldResponse,
    SpecificationFieldUpdate,
)

from app.services.specification_field_service import (
    SpecificationFieldService,
)


router = APIRouter(
    prefix="/specification-field",
    tags=["Specification Field"],
)


# ==========================
# GET ALL
# ==========================

@router.get(
    "/",
    response_model=list[SpecificationFieldResponse],
)
def get_all_fields(
    service: SpecificationFieldService = Depends(
        get_specification_field_service
    ),
):
    try:
        return service.get_all()

    except Exception as e:
        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# ==========================
# GET BY GROUP
# ==========================

@router.get(
    "/group/{group_id}",
    response_model=list[SpecificationFieldResponse],
)
def get_by_group(
    group_id: int,
    service: SpecificationFieldService = Depends(
        get_specification_field_service
    ),
):
    try:
        return service.get_by_group(
            group_id,
        )

    except Exception as e:
        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# ==========================
# GET BY ID
# ==========================

@router.get(
    "/{field_id}",
    response_model=SpecificationFieldResponse,
)
def get_field(
    field_id: int,
    service: SpecificationFieldService = Depends(
        get_specification_field_service
    ),
):

    try:

        field = service.get_by_id(
            field_id,
        )

        if field is None:
            raise HTTPException(
                status_code=404,
                detail="Specification Field not found.",
            )

        return field


    except HTTPException:
        raise


    except Exception as e:
        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# ==========================
# CREATE
# ==========================

@router.post(
    "/",
    response_model=SpecificationFieldResponse,
)
def create_field(
    field: SpecificationFieldCreate,
    service: SpecificationFieldService = Depends(
        get_specification_field_service
    ),
):

    try:

        return service.create(
            field,
        )


    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


    except Exception as e:

        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# ==========================
# UPDATE
# ==========================

@router.put(
    "/{field_id}",
    response_model=SpecificationFieldResponse,
)
def update_field(
    field_id: int,
    field: SpecificationFieldUpdate,
    service: SpecificationFieldService = Depends(
        get_specification_field_service
    ),
):

    try:

        updated = service.update(
            field_id,
            field,
        )


        if updated is None:

            raise HTTPException(
                status_code=404,
                detail="Specification Field not found.",
            )


        return updated


    except HTTPException:
        raise


    except Exception as e:

        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# ==========================
# DELETE
# ==========================

@router.delete(
    "/{field_id}",
)
def delete_field(
    field_id: int,
    service: SpecificationFieldService = Depends(
        get_specification_field_service
    ),
):

    try:

        deleted = service.delete(
            field_id,
        )


        if not deleted:

            raise HTTPException(
                status_code=404,
                detail="Specification Field not found.",
            )


        return {
            "message": "Specification Field deleted successfully."
        }


    except HTTPException:
        raise


    except Exception as e:

        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )