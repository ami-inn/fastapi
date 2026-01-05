"""FastAPI application for Omnicopy."""

from random import randint
from datetime import datetime, timezone
from typing import Annotated
from contextlib import asynccontextmanager
from sqlmodel import create_engine, SQLModel, Session, select, Field
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel


class Campaign(SQLModel, table=True):
    """Campaign model."""

    campaign_id: int | None = Field(default=None, primary_key=True)
    name: str
    due_date: datetime | None = Field(default=None, index=True)
    created_at: datetime | None = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=True, index=True
    )


SQLITE_FILE = "database.db"
SQLITE_URL = f"sqlite:///{SQLITE_FILE}"

connect_args = {"check_same_thread": False}  # only for SQLite
engine = create_engine(SQLITE_URL, connect_args=connect_args)


def create_db_and_tables():
    """Create database and tables."""
    SQLModel.metadata.create_all(engine)


def get_session():
    """Get a new database session."""
    with Session(engine) as session:
        yield session


session_dep = Annotated[Session, Depends(get_session)]


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager to create database and tables on startup."""
    create_db_and_tables()
    with Session(engine) as session:
        if not session.exec(select(Campaign)).first():
            session.add_all([
                Campaign(name="Summer Launch",due_date=datetime.now()),
                Campaign(name="Winter Sale",due_date=datetime.now()),
                Campaign(name="Spring Promotion",due_date=datetime.now()),
        ])
        session.commit()
    yield


app = FastAPI(root_path="/api/v1", lifespan=lifespan)

# Sample data for demonstration purposes
# list of dictionaries representing campaigns
data: list[dict[str, str | int]] = [
    {
        "campaign_id": 1,
        "name": "Campaign 1",
        "due_date": "2024-12-31",
        "created_at": "2024-01-01T12:00:00Z",
    },
    {
        "campaign_id": 2,
        "name": "Campaign 2",
        "due_date": "2024-11-30",
        "created_at": "2024-01-02T12:00:00Z",
    },
    {
        "campaign_id": 3,
        "name": "Campaign 3",
        "due_date": "2024-10-31",
        "created_at": "2024-01-03T12:00:00Z",
    },
    {
        "campaign_id": 4,
        "name": "Campaign 4",
        "due_date": "2024-09-30",
        "created_at": "2024-01-04T12:00:00Z",
    },
    {
        "campaign_id": 5,
        "name": "Campaign 5",
        "due_date": "2024-08-31",
        "created_at": "2024-01-05T12:00:00Z",
    },
    {
        "campaign_id": 6,
        "name": "Campaign 6",
        "due_date": "2024-07-31",
        "created_at": "2024-01-06T12:00:00Z",
    },
    {
        "campaign_id": 7,
        "name": "Campaign 7",
        "due_date": "2024-06-30",
        "created_at": "2024-01-07T12:00:00Z",
    },
    {
        "campaign_id": 8,
        "name": "Campaign 8",
        "due_date": "2024-05-31",
        "created_at": "2024-01-08T12:00:00Z",
    },
    {
        "campaign_id": 9,
        "name": "Campaign 9",
        "due_date": "2024-04-30",
        "created_at": "2024-01-09T12:00:00Z",
    },
    {
        "campaign_id": 10,
        "name": "Campaign 10",
        "due_date": "2024-03-31",
        "created_at": "2024-01-10T12:00:00Z",
    },
    {
        "campaign_id": 11,
        "name": "Campaign 11",
        "due_date": "2024-02-29",
        "created_at": "2024-01-11T12:00:00Z",
    },
]


# @app.get("/")
# async def read_root():
#     """Return a welcome message."""
#     return {"message": "Welcome to the Omnicopy API!"}


# @app.get("/campaigns")
# async def read_campaigns():
#     """Return a list of campaigns."""
#     return {"campaigns": data}


# @app.get("/campaigns/{campaign_id}")
# async def read_campaign(campaign_id: int):
#     """Return a specific campaign by ID."""
#     for campaign in data:
#         if campaign["campaign_id"] == campaign_id:
#             return {"campaign": campaign}
#     raise HTTPException(status_code=404, detail="Campaign not found")


# @app.post("/campaigns")
# async def create_campaign(body: dict[str, str]):
#     """create a new campaign."""

#     new: dict[str, str | int] = {
#         "campaign_id": randint(100, 1000),
#         "name": body.get("name", ""),
#         "due_date": body.get("due_date", ""),
#         "created_at": body.get("created_at", ""),
#     }

#     data.append(new)
#     return {"campaign": new}


# @app.put("/campaigns/{campaign_id}")
# async def update_campaign(campaign_id: int, body: dict[str, str]):
#     """Update an existing campaign by ID."""
#     for campaign in data:
#         if campaign["campaign_id"] == campaign_id:
#             campaign["name"] = body.get("name", campaign["name"])
#             campaign["due_date"] = body.get("due_date", campaign["due_date"])
#             campaign["created_at"] = campaign.get("created_at", campaign["created_at"])
#             return {"campaign": campaign}
#     raise HTTPException(status_code=404, detail="Campaign not found")


# @app.delete("/campaigns/{campaign_id}")
# async def delete_campaign(campaign_id: int):
#     """Delete a campaign by ID."""
#     for index, campaign in enumerate(
#         data
#     ):  # iterate with index enamurate means it gives index and value
#         if campaign["campaign_id"] == campaign_id:
#             del data[index]
#             return {"message": "Campaign deleted successfully"}
#     raise HTTPException(status_code=404, detail="Campaign not found")

class CampaignsResponse(BaseModel):
    """Response model for a list of campaigns."""

    campaigns: list[Campaign]

@app.get("/campaigns",response_model=CampaignsResponse)
async def read_campaigns(session: session_dep):
    """Return a list of campaigns from the database."""
    campaigns = session.exec(select(Campaign)).all()
    return {"campaigns": campaigns}

@app.post("/campaigns")
async def create_campaign(campaign: Campaign, session: session_dep):
    """Create a new campaign in the database."""
    session.add(campaign)
    session.commit()
    session.refresh(campaign)
    return {"campaign": campaign}
