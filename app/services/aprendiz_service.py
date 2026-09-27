from app.models.aprendiz_model import COLLECTION_NAME
from app.schemas.aprendiz_schema import AprendizCreate, AprendizUpdate


def listar(db):
    coleccion = db[COLLECTION_NAME]
    return list(coleccion.find({}, {"_id": 0}))


def buscar_por_id(db, aprendiz_id: int):
    coleccion = db[COLLECTION_NAME]
    return coleccion.find_one({"id": aprendiz_id}, {"_id": 0})


def _siguiente_id(coleccion):
    ultimo = coleccion.find_one(sort=[("id", -1)])
    return (ultimo["id"] + 1) if ultimo else 1


def crear(db, aprendiz: AprendizCreate):
    coleccion = db[COLLECTION_NAME]
    nuevo = aprendiz.model_dump()
    nuevo["id"] = _siguiente_id(coleccion)
    coleccion.insert_one(nuevo)
    nuevo.pop("_id", None)
    return nuevo


def actualizar(db, aprendiz_id: int, aprendiz: AprendizUpdate):
    coleccion = db[COLLECTION_NAME]
    existente = buscar_por_id(db, aprendiz_id)
    if not existente:
        return None
    cambios = aprendiz.model_dump(exclude_unset=True)
    coleccion.update_one({"id": aprendiz_id}, {"$set": cambios})
    return buscar_por_id(db, aprendiz_id)


def eliminar(db, aprendiz_id: int):
    coleccion = db[COLLECTION_NAME]
    existente = buscar_por_id(db, aprendiz_id)
    if not existente:
        return None
    coleccion.delete_one({"id": aprendiz_id})
    return existente