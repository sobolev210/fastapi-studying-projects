from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/pattern-types/", response_model=list[schemas.PatternType])  # this is  path operation decorator
def get_pattern_types(db: Session = Depends(get_db)):  # this is path operation function
    return crud.get_pattern_types(db)


@app.get("/pattern-types/{pattern_type_id}/", response_model=schemas.PatternType)
def get_pattern_type(pattern_type_id: int, db: Session = Depends(get_db)):
    db_pattern_type = crud.get_pattern_type(db, pattern_type_id=pattern_type_id)
    if db_pattern_type is None:
        raise HTTPException(status_code=404, detail="Pattern type not found.")
    return db_pattern_type


@app.post("/pattern-types/", response_model=schemas.PatternType)
def create_pattern_type(pattern_type: schemas.PatternTypeCreate, db: Session = Depends(get_db)):
    db_pattern_type = crud.create_pattern_type(db, pattern_type=pattern_type)
    return db_pattern_type


@app.get("/patterns/", response_model=list[schemas.Pattern])
def get_patterns(db: Session = Depends(get_db)):
    return crud.get_patterns(db)


@app.get("/patterns/{pattern_id:int}/", response_model=schemas.Pattern)
def get_pattern(pattern_id: int, db: Session = Depends(get_db)):
    db_pattern = crud.get_pattern(db, pattern_id=pattern_id)
    if db_pattern is None:
        raise HTTPException(status_code=404, detail="Pattern not found.")
    return db_pattern


@app.get("/patterns/{pattern_name:str}/", response_model=schemas.Pattern)
def get_pattern_by_name(pattern_name: str, db: Session = Depends(get_db)):
    db_pattern = crud.get_pattern_by_name(db, pattern_name=pattern_name)
    if db_pattern is None:
        raise HTTPException(status_code=404, detail="Pattern not found.")
    return db_pattern


@app.post("/patterns/", response_model=schemas.Pattern)
def create_pattern(pattern: schemas.PatternCreate, db: Session = Depends(get_db)):
    db_pattern = crud.create_pattern(db, pattern=pattern)
    return db_pattern


@app.get("/patterns/{pattern_id}/use-cases/", response_model=list[schemas.UseCase])
def get_use_cases_by_pattern(pattern_id: int, db: Session = Depends(get_db)):
    return crud.get_use_cases_by_pattern(db, pattern_id=pattern_id)


@app.get("/patterns/{pattern_id}/use-cases/{use_case_id}/", response_model=schemas.UseCase)
def get_use_case(pattern_id: int, use_case_id: int, db: Session = Depends(get_db)):
    db_use_case = crud.get_use_case(db, pattern_id=pattern_id, use_case_id=use_case_id)
    if db_use_case is None:
        raise HTTPException(status_code=404, detail="Use case not found.")
    return db_use_case


@app.post("/patterns/{pattern_id}/use-cases/", response_model=schemas.UseCase)
def create_use_case(pattern_id: int, use_case: schemas.UseCaseCreate, db: Session = Depends(get_db)):
    db_use_case = crud.create_use_case(db, pattern_id=pattern_id, use_case=use_case)
    return db_use_case

