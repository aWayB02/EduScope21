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
    clusterName: str = None
    row: str = None
    number: int = None
    rank: int = None
    campus: dict = None
    coalitionId: int = None
