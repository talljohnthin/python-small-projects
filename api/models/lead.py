import ormar
from typing import Optional
from datetime import datetime
from api.database import metadata, database


class Leads(ormar.Model):
    class Meta:
        tablename = "leads"
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)
    created_date: datetime = ormar.DateTime(default=datetime.now())
    updated_date: datetime = ormar.DateTime(default=datetime.now())
    firstname: str = ormar.String(max_length=255)
    lastname: str = ormar.String(max_length=255)
    emailaddress: str = ormar.String(max_length=255)
    phonenumber: str = ormar.String(max_length=255)
    zipcode: str = ormar.String(max_length=255)
    debtamount: str = ormar.String(max_length=255)
    income: str = ormar.String(max_length=255)
    valid: bool = ormar.Boolean()
    redirecturl: Optional[str] = ormar.String(max_length=255, nullable=True)
    ipaddress: Optional[str] = ormar.String(max_length=255, nullable=True)
    subid: str = ormar.String(max_length=255)
    useragent: str = ormar.String(max_length=2000)
