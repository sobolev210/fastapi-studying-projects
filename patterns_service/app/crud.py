from sqlalchemy.orm import Session

from . import models, schemas


def get_pattern_types(db: Session):
    return db.query(models.PatternType).all()


def get_pattern_type(db: Session, pattern_type_id: int):
    return db.query(models.PatternType).filter(models.PatternType.id == pattern_type_id).first()


def create_pattern_type(db: Session, pattern_type: schemas.PatternTypeCreate):
    db_pattern_type = models.PatternType(**pattern_type.dict())
    db.add(db_pattern_type)
    db.commit()
    db.refresh(db_pattern_type)
    return db_pattern_type


def get_patterns(db: Session):
    return db.query(models.Pattern).all()


def get_pattern(db: Session, pattern_id: int):
    return db.query(models.Pattern).filter(models.Pattern.id == pattern_id).first()


def get_pattern_by_name(db: Session, pattern_name: str):
    return db.query(models.Pattern).filter(models.Pattern.name == pattern_name).first()


def create_pattern(db: Session, pattern: schemas.PatternCreate):
    # need to add some validation that pattern type with this id exists
    db_pattern = models.Pattern(**pattern.dict())
    db.add(db_pattern)
    db.commit()
    db.refresh(db_pattern)
    return db_pattern


def get_use_cases_by_pattern(db: Session, pattern_id: int):
    return db.query(models.UseCase).filter(models.UseCase.pattern_id == pattern_id).all()


def get_use_case(db: Session, pattern_id: int, use_case_id: int, ):
    return db.query(models.UseCase).filter(
        models.UseCase.id == use_case_id,
        models.UseCase.pattern_id == pattern_id
    ).first()


def create_use_case(db: Session, use_case: schemas.UseCaseCreate, pattern_id: int):
    # need to add some validation that pattern with this id exists
    db_use_case = models.UseCase(**use_case.dict(), pattern_id=pattern_id)
    db.add(db_use_case)
    db.commit()
    db.refresh(db_use_case)
    return db_use_case
