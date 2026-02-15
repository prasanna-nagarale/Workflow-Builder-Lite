from fastapi import APIRouter, HTTPException
from app.database import SessionLocal
from app.models import Workflow
from app.schemas import WorkflowCreate
import json

router = APIRouter()

@router.post("/")
def create_workflow(data: WorkflowCreate):
    """Create a new workflow"""
    db = SessionLocal()
    try:
        workflow = Workflow(
            name=data.name,
            steps=json.dumps(data.steps)
        )
        db.add(workflow)
        db.commit()
        db.refresh(workflow)
        return {
            "message": "Workflow created successfully",
            "id": workflow.id,
            "name": workflow.name
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()

@router.get("/")
def list_workflows():
    """Get all workflows"""
    db = SessionLocal()
    try:
        workflows = db.query(Workflow).order_by(Workflow.created_at.desc()).all()
        return [
            {
                "id": w.id,
                "name": w.name,
                "steps": json.loads(w.steps),
                "created_at": w.created_at.isoformat()
            }
            for w in workflows
        ]
    finally:
        db.close()

@router.get("/{workflow_id}")
def get_workflow(workflow_id: int):
    """Get a specific workflow"""
    db = SessionLocal()
    try:
        workflow = db.query(Workflow).filter(Workflow.id == workflow_id).first()
        if not workflow:
            raise HTTPException(status_code=404, detail="Workflow not found")
        return {
            "id": workflow.id,
            "name": workflow.name,
            "steps": json.loads(workflow.steps),
            "created_at": workflow.created_at.isoformat()
        }
    finally:
        db.close()