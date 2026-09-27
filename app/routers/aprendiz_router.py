from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from app.schemas.aprendiz_schema import AprendizCreate, AprendizUpdate, AprendizOut
from app.services import aprendiz_service

router = APIRouter(prefix="/api/v1/aprendiz", tags=["Aprendices"])


@router.get("/", response_model=list[AprendizOut])
def listar(db=Depends(get_db)):
    return aprendiz_service.listar(db)


@router.get("/{aprendiz_id}", response_model=AprendizOut)
def buscar_por_id(aprendiz_id: int, db=Depends(get_db)):
    aprendiz = aprendiz_service.buscar_por_id(db, aprendiz_id)
    if not aprendiz:
        raise HTTPException(status_code=404, detail="Aprendiz no encontrado")
    return aprendiz


@router.post("/", response_model=AprendizOut, status_code=201)
def crear(aprendiz: AprendizCreate, db=Depends(get_db)):
    return aprendiz_service.crear(db, aprendiz)


@router.put("/{aprendiz_id}", response_model=AprendizOut)
def actualizar(aprendiz_id: int, aprendiz: AprendizUpdate, db=Depends(get_db)):
    actualizado = aprendiz_service.actualizar(db, aprendiz_id, aprendiz)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Aprendiz no encontrado")
    return actualizado


@router.delete("/{aprendiz_id}", status_code=204)
def eliminar(aprendiz_id: int, db=Depends(get_db)):
    eliminado = aprendiz_service.eliminar(db, aprendiz_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Aprendiz no encontrado")