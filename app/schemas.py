from pydantic import BaseModel, Field
from typing import List

class WorkflowCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    steps: List[str] = Field(..., min_items=1, max_items=5)

class RunCreate(BaseModel):
    workflow_id: int = Field(..., gt=0)
    input_text: str = Field(..., min_length=1)