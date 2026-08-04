"""
Formula Rule API.

REST API endpoints
for Formula Rule Management.
"""

import traceback

from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies.service import (
    get_formula_rule_service,
)

from app.schemas.formula_rule import (
    FormulaRuleCreate,
    FormulaRuleUpdate,
    FormulaRuleResponse,
)

from app.services.formula_rule_service import (
    FormulaRuleService,
)

router = APIRouter(
    prefix="/formula-rule",
    tags=["Formula Rule"],
)


# ==========================================
# GET ALL
# ==========================================

@router.get(
    "/",
    response_model=list[FormulaRuleResponse],
)
def get_all_rules(
    service: FormulaRuleService = Depends(
        get_formula_rule_service,
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
    response_model=list[FormulaRuleResponse],
)
def get_by_template(
    template_id: int,
    service: FormulaRuleService = Depends(
        get_formula_rule_service,
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


# ==========================================
# GET BY ID
# ==========================================

@router.get(
    "/{formula_id}",
    response_model=FormulaRuleResponse,
)
def get_rule(
    formula_id: int,
    service: FormulaRuleService = Depends(
        get_formula_rule_service,
    ),
):
    try:

        rule = service.get_by_id(
            formula_id,
        )

        if rule is None:
            raise HTTPException(
                status_code=404,
                detail="Formula Rule not found.",
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
    response_model=FormulaRuleResponse,
)
def create_rule(
    rule: FormulaRuleCreate,
    service: FormulaRuleService = Depends(
        get_formula_rule_service,
    ),
):
    try:
        return service.create(rule)

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


# ==========================================
# UPDATE
# ==========================================

@router.put(
    "/{formula_id}",
    response_model=FormulaRuleResponse,
)
def update_rule(
    formula_id: int,
    rule: FormulaRuleUpdate,
    service: FormulaRuleService = Depends(
        get_formula_rule_service,
    ),
):
    try:

        updated = service.update(
            formula_id,
            rule,
        )

        if updated is None:
            raise HTTPException(
                status_code=404,
                detail="Formula Rule not found.",
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
    "/{formula_id}",
)
def delete_rule(
    formula_id: int,
    service: FormulaRuleService = Depends(
        get_formula_rule_service,
    ),
):
    try:

        deleted = service.delete(
            formula_id,
        )

        if not deleted:
            raise HTTPException(
                status_code=404,
                detail="Formula Rule not found.",
            )

        return {
            "message": "Formula Rule deleted successfully."
        }

    except HTTPException:
        raise

    except Exception as e:
        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )