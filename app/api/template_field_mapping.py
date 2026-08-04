"""
MKPrintingMasterPro ERP
Build-016

Template Field Mapping API

REST API endpoints
for Template Field Mapping Management.
"""

import traceback

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from app.api.dependencies.service import (
    get_template_field_mapping_service,
)

from app.schemas.template_field_mapping import (
    TemplateFieldMappingCreate,
    TemplateFieldMappingUpdate,
    TemplateFieldMappingResponse,
)

from app.services.template_field_mapping_service import (
    TemplateFieldMappingService,
)


router = APIRouter(
    prefix="/template-field-mapping",
    tags=["Template Field Mapping"],
)



# ==========================================
# GET ALL
# ==========================================

@router.get(
    "/",
    response_model=list[TemplateFieldMappingResponse],
)
def get_all_mappings(
    service: TemplateFieldMappingService = Depends(
        get_template_field_mapping_service
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



# ==========================================
# GET BY TEMPLATE
# ==========================================

@router.get(
    "/template/{template_id}",
    response_model=list[TemplateFieldMappingResponse],
)
def get_by_template(
    template_id: int,
    service: TemplateFieldMappingService = Depends(
        get_template_field_mapping_service
    ),
):

    try:

        return service.get_by_template(
            template_id
        )


    except Exception as e:

        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )



# ==========================================
# GET BY ID
# ==========================================

@router.get(
    "/{mapping_id}",
    response_model=TemplateFieldMappingResponse,
)
def get_mapping(
    mapping_id: int,
    service: TemplateFieldMappingService = Depends(
        get_template_field_mapping_service
    ),
):

    try:

        mapping = service.get_by_id(
            mapping_id
        )


        if mapping is None:

            raise HTTPException(
                status_code=404,
                detail="Template Field Mapping not found.",
            )


        return mapping


    except HTTPException:
        raise


    except Exception as e:

        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )



# ==========================================
# CREATE
# ==========================================

@router.post(
    "/",
    response_model=TemplateFieldMappingResponse,
)
def create_mapping(
    mapping: TemplateFieldMappingCreate,
    service: TemplateFieldMappingService = Depends(
        get_template_field_mapping_service
    ),
):

    try:

        return service.create(
            mapping
        )


    except Exception as e:

        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )



# ==========================================
# UPDATE
# ==========================================

@router.put(
    "/{mapping_id}",
    response_model=TemplateFieldMappingResponse,
)
def update_mapping(
    mapping_id: int,
    mapping: TemplateFieldMappingUpdate,
    service: TemplateFieldMappingService = Depends(
        get_template_field_mapping_service
    ),
):

    try:

        updated = service.update(
            mapping_id,
            mapping,
        )


        if updated is None:

            raise HTTPException(
                status_code=404,
                detail="Template Field Mapping not found.",
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



# ==========================================
# DELETE
# ==========================================

@router.delete(
    "/{mapping_id}",
)
def delete_mapping(
    mapping_id: int,
    service: TemplateFieldMappingService = Depends(
        get_template_field_mapping_service
    ),
):

    try:

        deleted = service.delete(
            mapping_id
        )


        if not deleted:

            raise HTTPException(
                status_code=404,
                detail="Template Field Mapping not found.",
            )


        return {
            "message": "Template Field Mapping deleted successfully."
        }


    except HTTPException:
        raise


    except Exception as e:

        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )