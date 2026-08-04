"""
Specification Group API.

REST API endpoints
for Specification Group Management.
"""

import traceback

from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies.service import (
    get_specification_group_service,
)

from app.schemas.specification_group import (
    SpecificationGroupCreate,
    SpecificationGroupResponse,
    SpecificationGroupUpdate,
)

from app.services.specification_group_service import (
    SpecificationGroupService,
)


router = APIRouter(
    prefix="/specification-group",
    tags=["Specification Group"],
)


@router.get(
    "/",
    response_model=list[SpecificationGroupResponse],
)
def get_all_groups(
    service: SpecificationGroupService = Depends(
        get_specification_group_service
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


@router.get(
    "/template/{template_id}",
    response_model=list[SpecificationGroupResponse],
)
def get_groups_by_template(
    template_id: int,
    service: SpecificationGroupService = Depends(
        get_specification_group_service
    ),
):
    try:
        return service.get_by_template(
            template_id,
        )

    except Exception as e:
        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


@router.get(
    "/{group_id}",
    response_model=SpecificationGroupResponse,
)
def get_group(
    group_id: int,
    service: SpecificationGroupService = Depends(
        get_specification_group_service
    ),
):
    try:
        group = service.get_by_id(
            group_id,
        )

        if group is None:
            raise HTTPException(
                status_code=404,
                detail="Specification Group not found.",
            )

        return group

    except HTTPException:
        raise

    except Exception as e:
        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


@router.post(
    "/",
    response_model=SpecificationGroupResponse,
)
def create_group(
    group: SpecificationGroupCreate,
    service: SpecificationGroupService = Depends(
        get_specification_group_service
    ),
):
    try:
        return service.create(
            group,
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


@router.put(
    "/{group_id}",
    response_model=SpecificationGroupResponse,
)
def update_group(
    group_id: int,
    group: SpecificationGroupUpdate,
    service: SpecificationGroupService = Depends(
        get_specification_group_service
    ),
):
    try:
        updated = service.update(
            group_id,
            group,
        )

        if updated is None:
            raise HTTPException(
                status_code=404,
                detail="Specification Group not found.",
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


@router.delete(
    "/{group_id}",
)
def delete_group(
    group_id: int,
    service: SpecificationGroupService = Depends(
        get_specification_group_service
    ),
):
    try:
        deleted = service.delete(
            group_id,
        )

        if not deleted:
            raise HTTPException(
                status_code=404,
                detail="Specification Group not found.",
            )

        return {
            "message": "Specification Group deleted successfully."
        }

    except HTTPException:
        raise

    except Exception as e:
        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )