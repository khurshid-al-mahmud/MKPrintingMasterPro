"""
Field Option API.

REST API endpoints
for Dynamic Field Option Management.
"""

import traceback

from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies.service import (
    get_field_option_service,
)

from app.schemas.field_option import (
    FieldOptionCreate,
    FieldOptionUpdate,
    FieldOptionResponse,
)

from app.services.field_option_service import (
    FieldOptionService,
)

router = APIRouter(
    prefix="/field-option",
    tags=["Field Option"],
)


# ==========================
# GET ALL
# ==========================

@router.get(
    "/",
    response_model=list[FieldOptionResponse],
)
def get_all_options(
    service: FieldOptionService = Depends(
        get_field_option_service
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
# GET BY FIELD
# ==========================

@router.get(
    "/field/{field_id}",
    response_model=list[FieldOptionResponse],
)
def get_by_field(
    field_id: int,
    service: FieldOptionService = Depends(
        get_field_option_service
    ),
):
    try:
        return service.get_by_field(field_id)

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
    "/{option_id}",
    response_model=FieldOptionResponse,
)
def get_option(
    option_id: int,
    service: FieldOptionService = Depends(
        get_field_option_service
    ),
):
    try:

        option = service.get_by_id(option_id)

        if option is None:
            raise HTTPException(
                status_code=404,
                detail="Field Option not found.",
            )

        return option

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
    response_model=FieldOptionResponse,
)
def create_option(
    option: FieldOptionCreate,
    service: FieldOptionService = Depends(
        get_field_option_service
    ),
):
    try:
        return service.create(option)

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
    "/{option_id}",
    response_model=FieldOptionResponse,
)
def update_option(
    option_id: int,
    option: FieldOptionUpdate,
    service: FieldOptionService = Depends(
        get_field_option_service
    ),
):
    try:

        updated = service.update(
            option_id,
            option,
        )

        if updated is None:
            raise HTTPException(
                status_code=404,
                detail="Field Option not found.",
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
    "/{option_id}",
)
def delete_option(
    option_id: int,
    service: FieldOptionService = Depends(
        get_field_option_service
    ),
):
    try:

        deleted = service.delete(option_id)

        if not deleted:
            raise HTTPException(
                status_code=404,
                detail="Field Option not found.",
            )

        return {
            "message": "Field Option deleted successfully."
        }

    except HTTPException:
        raise

    except Exception as e:

        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )