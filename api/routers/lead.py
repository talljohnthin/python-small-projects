from datetime import datetime, date, timedelta
from fastapi import APIRouter, status, HTTPException
from typing import List
from api.models.lead import Leads

router = APIRouter(tags=["Leads"])

options = {"limit": 10}


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[Leads])
async def get_leads(page: int = 1):
    leads = await Leads.objects.paginate(page, options["limit"]).all()
    # if len(leads) <= 0:
    #     raise HTTPException(status_code=404, detail="Item not found")
    return leads


@router.get("/today", status_code=status.HTTP_200_OK, response_model=List[Leads])
async def get_leads(page: int = 1):
    leads = await Leads.objects.paginate(page, options["limit"]).filter(
        Leads.created_date > f'{date.today()}T00:00:00.000Z'
    ).order_by("created_date").all()
    if len(leads) <= 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return leads


@router.get("/yesterday", status_code=status.HTTP_200_OK, response_model=List[Leads])
async def get_leads(page: int = 1):
    date_yesterday = date.today() - timedelta(1)
    leads = await Leads.objects.paginate(page, options["limit"]).filter(
        (Leads.created_date > f'{date_yesterday}T00:00:00.000Z') & (
            Leads.created_date < f'{date_yesterday}T23:59:00.000Z')
    ).order_by("created_date").all()
    # if len(leads) <= 0:
    #     raise HTTPException(status_code=404, detail="Item not found")
    return leads


@router.get("/one-week-ago", status_code=status.HTTP_200_OK, response_model=List[Leads])
async def get_leads(page: int = 1):
    date_7_days_ago = date.today() - timedelta(7)
    leads = await Leads.objects.paginate(page, options["limit"]).filter(
        Leads.created_date > f'{date_7_days_ago}T00:00:00.000Z'
    ).order_by("created_date").all()
    # if len(leads) <= 0:
    #     raise HTTPException(status_code=404, detail="Item not found")
    return leads


@router.get("/week-to-date", status_code=status.HTTP_200_OK, response_model=List[Leads])
async def get_leads(page: int = 1):
    today = date.today()
    start = today + timedelta(days=-today.weekday(),
                              weeks=-1)  # last week monday
    end = start + timedelta(days=6)  # last week sunday
    leads = await Leads.objects.paginate(page, options["limit"]).filter(
        (Leads.created_date > f'{start}T00:00:00.000Z') & (
            Leads.created_date < f'{end}T23:59:00.000Z')
    ).order_by("created_date").all()
    # if len(leads) <= 0:
    #     raise HTTPException(status_code=404, detail="Item not found")
    return leads


@router.get("/current-month", status_code=status.HTTP_200_OK, response_model=List[Leads])
async def get_leads(page: int = 1):
    first_day_of_the_month = datetime.today().replace(day=1).date()
    leads = await Leads.objects.paginate(page, options["limit"]).filter(
        Leads.created_date > f'{first_day_of_the_month}T00:00:00.000Z'
    ).order_by("created_date").all()
    # if len(leads) <= 0:
    #     raise HTTPException(status_code=404, detail="Item not found")
    return leads


@router.get("/last-month", status_code=status.HTTP_200_OK, response_model=List[Leads])
async def get_leads(page: int = 1):
    last_day_of_prev_month = date.today().replace(day=1) - timedelta(days=1)
    start_day_of_prev_month = date.today().replace(
        day=1) - timedelta(days=last_day_of_prev_month.day)
    print(start_day_of_prev_month)
    print(last_day_of_prev_month)
    leads = await Leads.objects.paginate(page, options["limit"]).filter(
        (Leads.created_date > f'{start_day_of_prev_month}T00:00:00.000Z') & (
            Leads.created_date < f'{last_day_of_prev_month}T23:59:00.000Z')
    ).order_by("created_date").all()
    # if len(leads) <= 0:
    #     raise HTTPException(status_code=404, detail="Item not found")
    return leads


@router.get("/one-year-ago", status_code=status.HTTP_200_OK, response_model=List[Leads])
async def get_leads(page: int = 1):
    last_year = date.today().year - 1
    leads = await Leads.objects.paginate(page, options["limit"]).filter(
        Leads.created_date > f'{last_year}-01-01T00:00:00.000Z'
    ).order_by("created_date").all()
    # if len(leads) <= 0:
    #     raise HTTPException(status_code=404, detail="Item not found")
    return leads
