from app.database.engine import engine
from app.models.base import Base

# Import all models
from app.models import (
    Party,
    CustomerProfile,
    SupplierProfile,
    EmployeeProfile,
    PrintPartnerProfile,
    PartyContact,
    PartyRole,
    NumberSequence,
)


def create_tables():

    print("Creating database tables...")

    Base.metadata.create_all(
        bind=engine
    )

    print("Database tables created successfully!")


if __name__ == "__main__":

    create_tables()