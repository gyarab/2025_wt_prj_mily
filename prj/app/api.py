from ninja import NinjaAPI
from .models import Recept
from ninja import Schema

api = NinjaAPI()

class ReceptSchema(Schema):
    id: int
    nazev: str
    popis: str
    kategorie: int
    autor: int

@api.get("/recepty", response=list[ReceptSchema])
def get_recepty(request):
    return Recept.objects.all()