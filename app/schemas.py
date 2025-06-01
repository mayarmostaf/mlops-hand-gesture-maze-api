from pydantic import BaseModel
from typing import List

class HandLandmarks(BaseModel):
    landmarks: List[float] 