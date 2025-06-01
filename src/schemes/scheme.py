from pydantic import BaseModel
from typing import Optional


class Participant(BaseModel):
    login: str
    name: str
    coins: int
    peerReviewPoints: int
    codeReviewPoints: int
    className: str
    parallelName: str
    expValue: int
    level: int
    expToNextLevel: int
    active: Optional[bool] = None
    clusterName: Optional[str] = None
    row: Optional[str] = None
    number: Optional[int] = None
    rank: Optional[int] = None
    campus: Optional[dict] = None
    coalitionId: Optional[int] = None
    logtime: int
