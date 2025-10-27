from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field, constr
from typing import Optional, List
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

# ---------- Configuración MongoDB ----------
MONGO_URI = "mongodb://admin:123@mongodb:27017/?authSource=admin"
DB_NAME = "reservas_db"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
reservas_col = db.get_collection("reservas")

# ---------- Modelos ----------
Telefono = constr(strip_whitespace=True, min_length=6, max_length=20)

class ReservaIn(BaseModel):
    nombre: constr(strip_whitespace=True, min_length=2)
    telefono: Telefono
    personas: int = Field(..., ge=1, le=20)
    restaurante: constr(strip_whitespace=True, min_length=2)
    fecha_hora: datetime
    notas: Optional[str] = None

class ReservaOut(ReservaIn):
    id: str

# ---------- Función auxiliar ----------
def to_out(doc: dict) -> dict:
    doc["id"] = str(doc["_id"])
    doc.pop("_id", None)
    return doc

# ---------- App principal ----------
app = FastAPI(
    title="API Reservas Restaurante ",
    description="CRUD mínimo con FastAPI + MongoDB",
    version="1.0.0",
)

@app.on_event("startup")
async def init_indexes():
    # Índice único para evitar duplicados exactos (restaurante, fecha_hora)
    await reservas_col.create_index(
        [("restaurante", 1), ("fecha_hora", 1)],
        name="uniq_rest_fh",
        unique=True
    )

# ---------- Endpoints ----------
@app.get("/reservas", response_model=List[ReservaOut])
async def listar_reservas(
    skip: int = 0,
    limit: int = Query(50, le=200),
    restaurante: Optional[str] = None
):
    filtro = {"restaurante": restaurante} if restaurante else {}
    items = []
    cursor = reservas_col.find(filtro, skip=skip, limit=limit).sort("fecha_hora", 1)
    async for doc in cursor:
        items.append(to_out(doc))
    return items

@app.post("/reservas", response_model=ReservaOut, status_code=201)
async def crear_reserva(payload: ReservaIn):
    # Verificamos duplicado exacto
    existe = await reservas_col.find_one({
        "restaurante": payload.restaurante,
        "fecha_hora": payload.fecha_hora
    })
    if existe:
        raise HTTPException(409, "Ya existe una reserva en ese restaurante a esa hora")

    res = await reservas_col.insert_one(payload.model_dump())
    doc = await reservas_col.find_one({"_id": res.inserted_id})
    return to_out(doc)

@app.delete("/reservas/{id}", status_code=204)
async def borrar_reserva(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(400, "ID inválido")
    res = await reservas_col.delete_one({"_id": ObjectId(id)})
    if res.deleted_count == 0:
        raise HTTPException(404, "Reserva no encontrada")
    return

