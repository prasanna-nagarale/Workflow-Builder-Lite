from fastapi import APIRouter, HTTPException
from app.database import SessionLocal
from app.models import Run, Workflow
from app.schemas import RunCreate
from app.workflow_runner import run_workflow
import json

router = APIRouter()

@router.post("/")
def execute_run(data: RunCreate):
    """Execute a workflow run"""
    db = SessionLocal()
    try:
        workflow = db.query(Workflow).filter(Workflow.id == data.workflow_id).first()
        
        if not workflow:
            raise HTTPException(status_code=404, detail="Workflow not found")

        steps = json.loads(workflow.steps)
        outputs = run_workflow(steps, data.input_text)

        run_obj = Run(
            workflow_id=data.workflow_id,
            workflow_name=workflow.name,
            input_text=data.input_text,
            outputs=json.dumps(outputs)
        )
        db.add(run_obj)
        db.commit()

        return outputs
        
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Execution failed: {str(e)}")
    finally:
        db.close()

@router.get("/history")
def get_history():
    """Get last 5 workflow runs"""
    db = SessionLocal()
    try:
        runs = db.query(Run).order_by(Run.created_at.desc()).limit(5).all()
        return [
            {
                "id": r.id,
                "workflow_id": r.workflow_id,
                "workflow_name": r.workflow_name,
                "input_preview": r.input_text[:100] + "..." if len(r.input_text) > 100 else r.input_text,
                "created_at": r.created_at.isoformat()
            }
            for r in runs
        ]
    finally:
        db.close()

@router.get("/{run_id}")
def get_run_details(run_id: int):
    """Get detailed run results"""
    db = SessionLocal()
    try:
        run = db.query(Run).filter(Run.id == run_id).first()
        if not run:
            raise HTTPException(status_code=404, detail="Run not found")
        
        return {
            "id": run.id,
            "workflow_name": run.workflow_name,
            "input_text": run.input_text,
            "outputs": json.loads(run.outputs),
            "created_at": run.created_at.isoformat()
        }
    finally:
        db.close()