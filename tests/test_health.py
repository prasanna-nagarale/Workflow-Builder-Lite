import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home_page():
    """Test home page loads"""
    response = client.get("/")
    assert response.status_code == 200

def test_status_endpoint():
    """Test status endpoint returns correct structure"""
    response = client.get("/api/status")
    assert response.status_code == 200
    data = response.json()
    assert "backend" in data
    assert "database" in data
    assert "llm_provider" in data
    assert data["backend"] == "OK"

def test_list_workflows_empty():
    """Test listing workflows when none exist"""
    response = client.get("/api/workflows/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_create_workflow():
    """Test creating a new workflow"""
    workflow_data = {
        "name": "Test Workflow",
        "steps": ["Clean Text", "Summarize"]
    }
    response = client.post("/api/workflows/", json=workflow_data)
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Workflow created successfully"

def test_create_workflow_validation():
    """Test workflow creation with invalid data"""
    # Empty name
    response = client.post("/api/workflows/", json={"name": "", "steps": ["Clean Text"]})
    assert response.status_code == 422
    
    # Empty steps
    response = client.post("/api/workflows/", json={"name": "Test", "steps": []})
    assert response.status_code == 422

def test_run_workflow_not_found():
    """Test running non-existent workflow"""
    run_data = {
        "workflow_id": 99999,
        "input_text": "Test text"
    }
    response = client.post("/api/runs/", json=run_data)
    assert response.status_code == 404

def test_run_history():
    """Test getting run history"""
    response = client.get("/api/runs/history")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)