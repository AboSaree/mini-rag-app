from pydantic import BaseModel
from typing import Optional
class ProcessScheme(BaseModel):
    file_id: str
    chunk_size: Optional[int] = 100
    overlap_size: Optional[int] = 20
    do_reset: int = 0