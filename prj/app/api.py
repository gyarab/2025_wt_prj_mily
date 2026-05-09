from ninja import NinjaAPI, Schema
from .models import Recept
from  ninja import Schema, NinjaAPI

api = NinjaAPI()


class ReceptSchema(Schema):
    id: int
    nazev: str
    popis: str
    kategorie: int
    autor: int


class ReceptCreateSchema(Schema):
    nazev: str
    popis: str


# GET seznam
@api.get("/recepty", response=list[ReceptSchema])
def get_recepty(request):
    return Recept.objects.all()


# GET detail
@api.get("/recepty/{recept_id}", response=ReceptSchema)
def get_recept(request, recept_id: int):
    return Recept.objects.get(id=recept_id)


# POST vytvoření
@api.post("/recepty")
def create_recept(request, data: ReceptCreateSchema):

    recept = Recept.objects.create(
        nazev=data.nazev,
        popis=data.popis,
        kategorie_id=1,
        autor_id=1
    )

    return {"id": recept.id}


# PUT úprava
@api.put("/recepty/{recept_id}")
def update_recept(request, recept_id: int, data: ReceptCreateSchema):

    recept = Recept.objects.get(id=recept_id)

    recept.nazev = data.nazev
    recept.popis = data.popis

    recept.save()

    return {"success": True}