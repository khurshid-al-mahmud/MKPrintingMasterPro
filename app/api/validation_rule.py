"""
MKPrintingMasterPro ERP

Build-013

Validation Rule API

Purpose:
REST API endpoints
for Validation Rule Management.
"""

import traceback

from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies.service import (
    get_validation_rule_service,
)

from app.schemas.validation_rule import (
    ValidationRuleCreate,
    ValidationRuleUpdate,
    ValidationRuleResponse,
)

from app.services.validation_rule_service import (
    ValidationRuleService,
)


router = APIRouter(
    prefix="/validation-rule",
    tags=["Validation Rule"],
)


# ==========================
# GET ALL
# ==========================

@router.get(
    "/",
    response_model=list[ValidationRuleResponse],
)
def get_all_rules(
    service: ValidationRuleService = Depends(
        get_validation_rule_service
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
    response_model=list[ValidationRuleResponse],
)
def get_by_field(
    field_id: int,
    service: ValidationRuleService = Depends(
        get_validation_rule_service
    ),
):

    try:

        return service.get_by_field(
            field_id
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
    "/{rule_id}",
    response_model=ValidationRuleResponse,
)
def get_rule(
    rule_id: int,
    service: ValidationRuleService = Depends(
        get_validation_rule_service
    ),
):

    try:

        rule = service.get_by_id(
            rule_id
        )

        if rule is None:

            raise HTTPException(
                status_code=404,
                detail="Validation Rule not found.",
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


# ==========================
# CREATE
# ==========================

@router.post(
    "/",
    response_model=ValidationRuleResponse,
)
def create_rule(
    rule: ValidationRuleCreate,
    service: ValidationRuleService = Depends(
        get_validation_rule_service
    ),
):

    try:

        return service.create(
            rule
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
    "/{rule_id}",
    response_model=ValidationRuleResponse,
)
def update_rule(
    rule_id: int,
    rule: ValidationRuleUpdate,
    service: ValidationRuleService = Depends(
        get_validation_rule_service
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
                detail="Validation Rule not found.",
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
    "/{rule_id}",
)
def delete_rule(
    rule_id: int,
    service: ValidationRuleService = Depends(
        get_validation_rule_service
    ),
):

    try:

        deleted = service.delete(
            rule_id
        )


        if not deleted:

            raise HTTPException(
                status_code=404,
                detail="Validation Rule not found.",
            )


        return {
            "message": "Validation Rule deleted successfully."
        }


    except HTTPException:

        raise


    except Exception as e:

        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )