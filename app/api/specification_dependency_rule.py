"""
MKPrintingMasterPro ERP
Build-015A

Specification Dependency Rule API

REST API endpoints
for Specification Dependency Rule Management.
"""

import traceback

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from app.api.dependencies.service import (
    get_specification_dependency_rule_service,
)

from app.schemas.specification_dependency_rule import (
    SpecificationDependencyRuleCreate,
    SpecificationDependencyRuleUpdate,
    SpecificationDependencyRuleResponse,
)

from app.services.specification_dependency_rule_service import (
    SpecificationDependencyRuleService,
)


router = APIRouter(
    prefix="/specification-dependency-rule",
    tags=["Specification Dependency Rule"],
)


# ==========================================
# GET ALL
# ==========================================

@router.get(
    "/",
    response_model=list[SpecificationDependencyRuleResponse],
)
def get_all_rules(
    service: SpecificationDependencyRuleService = Depends(
        get_specification_dependency_rule_service
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
    response_model=list[SpecificationDependencyRuleResponse],
)
def get_by_template(
    template_id: int,
    service: SpecificationDependencyRuleService = Depends(
        get_specification_dependency_rule_service
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
# GET BY SOURCE FIELD
# ==========================================

@router.get(
    "/source-field/{field_id}",
    response_model=list[SpecificationDependencyRuleResponse],
)
def get_by_source_field(
    field_id: int,
    service: SpecificationDependencyRuleService = Depends(
        get_specification_dependency_rule_service
    ),
):

    try:

        return service.get_by_source_field(
            field_id
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
    "/{rule_id}",
    response_model=SpecificationDependencyRuleResponse,
)
def get_rule(
    rule_id: int,
    service: SpecificationDependencyRuleService = Depends(
        get_specification_dependency_rule_service
    ),
):

    try:

        rule = service.get_by_id(
            rule_id
        )

        if rule is None:

            raise HTTPException(
                status_code=404,
                detail="Dependency Rule not found.",
            )

        return rule


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
    response_model=SpecificationDependencyRuleResponse,
)
def create_rule(
    rule: SpecificationDependencyRuleCreate,
    service: SpecificationDependencyRuleService = Depends(
        get_specification_dependency_rule_service
    ),
):

    try:

        return service.create(
            rule
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
    "/{rule_id}",
    response_model=SpecificationDependencyRuleResponse,
)
def update_rule(
    rule_id: int,
    rule: SpecificationDependencyRuleUpdate,
    service: SpecificationDependencyRuleService = Depends(
        get_specification_dependency_rule_service
    ),
):

    try:

        updated = service.update(
            rule_id,
            rule,
        )

        if updated is None:

            raise HTTPException(
                status_code=404,
                detail="Dependency Rule not found.",
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
    "/{rule_id}",
)
def delete_rule(
    rule_id: int,
    service: SpecificationDependencyRuleService = Depends(
        get_specification_dependency_rule_service
    ),
):

    try:

        deleted = service.delete(
            rule_id
        )

        if not deleted:

            raise HTTPException(
                status_code=404,
                detail="Dependency Rule not found.",
            )

        return {
            "message": "Dependency Rule deleted successfully."
        }


    except HTTPException:
        raise


    except Exception as e:

        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )