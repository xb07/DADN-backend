from pydantic import BaseModel
from typing import Dict, List


class Geometry(BaseModel):
    d1: float
    d2: float
    elementType: str
    bcType: str


class MeshConfig(BaseModel):
    p: int
    m: int


class PhysicalProperties(BaseModel):
    E: float
    nu: float
    planeState: str


class Loads(BaseModel):
    loadVal: float
    loadDirection: str


class SolveRequest(BaseModel):
    geometry: Geometry
    mesh: MeshConfig
    physical: PhysicalProperties
    loads: Loads


class SolveResult(BaseModel):
    job_id: str
    status: str
    displacements: Dict[str, float]
    max_displacement: float
    warnings: List[str]