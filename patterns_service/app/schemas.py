from pydantic import BaseModel


class PatternTypeBase(BaseModel):
    name: str


class PatternTypeCreate(PatternTypeBase):
    pass


class PatternType(PatternTypeBase):
    id: int

    class Config:
        orm_mode = True


class PatternBase(BaseModel):
    name: str
    intent: str
    description: str | None = None


class PatternCreate(PatternBase):
    pattern_type_id: int


class Pattern(PatternBase):
    id: int
    pattern_type: PatternType
    use_cases: list['UseCase']

    class Config:
        orm_mode = True


class UseCaseBase(BaseModel):
    description: str


class UseCaseCreate(UseCaseBase):
    pass


class UseCase(UseCaseBase):
    id: int

    class Config:
        orm_mode = True


Pattern.update_forward_refs()
