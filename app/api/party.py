"""
Party API.

REST API endpoints
for Party Management.
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/party",
    tags=["Party"],
)


@router.get(
    "/",
)
def get_all_parties():
    """
    Get all parties.
    """

    return {
        "message": "Get all parties"
    }


@router.get(
    "/{party_id}",
)
def get_party(
    party_id: int,
):
    """
    Get party by ID.
    """

    return {
        "message": f"Get party {party_id}"
    }




# ================= PART-2 HERE =================



@router.post(
    "/",
)
def create_party():
    """
    Create new party.
    """

    return {
        "message": "Create party"
    }


@router.put(
    "/{party_id}",
)
def update_party(
    party_id: int,
):
    """
    Update existing party.
    """

    return {
        "message": f"Update party {party_id}"
    }


@router.delete(
    "/{party_id}",
)
def delete_party(
    party_id: int,
):
    """
    Soft delete party.
    """

    return {
        "message": f"Delete party {party_id}"
    }




# ================= PART-3 HERE =================



@router.get(
    "/search/{keyword}",
)
def search_party(
    keyword: str,
):
    """
    Search parties.
    """

    return {
        "message": f"Search party: {keyword}"
    }