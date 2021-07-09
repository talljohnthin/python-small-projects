from fastapi import APIRouter, status
from typing import List, Optional
from jobscraping.scraper import scraper
from pydantic.main import BaseModel

router = APIRouter(tags=["Jobs"])


class Job(BaseModel):
    title: str
    link: str
    salary: Optional[str]
    company_location: Optional[str]


@router.get("/jobs", status_code=status.HTTP_200_OK, response_model=List[Job])
async def get_jobs(skill: str):
    return await scraper(skill)
