# 🚀 Workflow Builder Lite

A web application that allows users to create and run AI-powered text processing workflows with multiple sequential steps.

## ✨ Features

- **Workflow Creation**: Build custom workflows with 1-5 AI processing steps
- **Step Library**: 5 pre-configured AI steps (Clean Text, Summarize, Extract Key Points, Tag Category, Sentiment Analysis)
- **Sequential Processing**: Each step processes output from the previous step
- **Run History**: Track your last 5 workflow executions
- **System Status**: Monitor backend, database, and LLM connection health
- **Modern UI**: Clean, responsive interface with gradient design

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **LLM Provider**: Groq (Llama 3.3 70B Versatile) - Fast and free
- **Frontend**: Vanilla JavaScript, HTML5, CSS3
- **Hosting**: Deployable to Render, Railway, or any Python-supporting platform

## 📦 Installation

### Prerequisites
- Python 3.8+
- Groq API key (free from [console.groq.com](https://console.groq.com))

### Local Setup

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd workflow-builder-lite
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment**
```bash
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
```

4. **Run the application**
```bash
uvicorn app.main:app --reload
```

5. **Open browser**
```
http://127.0.0.1:8000
```



## 📖 Usage Guide

### 1. Create a Workflow
- Go to **Builder** page
- Name your workflow
- Select 1-5 steps in desired order
- Click "Create Workflow"

### 2. Run Workflow
- Go to **Run** page
- Select a workflow from dropdown
- Paste your text
- Click "Run Workflow"
- View step-by-step outputs

### 3. View History
- Check **History** page for last 5 runs
- See workflow name, input preview, and timestamp

### 4. Check Status
- Visit **Status** page
- Verify all systems are operational

## 🎯 Available Steps

| Step | Description |
|------|-------------|
| 🧹 Clean Text | Remove filler words, fix grammar, normalize formatting |
| 📝 Summarize | Generate 3-4 sentence summary |
| 🎯 Extract Key Points | Create 5-7 bullet points of main ideas |
| 🏷️ Tag Category | Classify into categories (Tech, Business, etc.) |
| 😊 Sentiment | Analyze emotional tone (Positive/Negative/Neutral/Mixed) |

## 📁 Project Structure

```
workflow-builder-lite/
├── app/
│   ├── main.py              # FastAPI application entry
│   ├── database.py          # SQLAlchemy setup
│   ├── models.py            # Database models
│   ├── schemas.py           # Pydantic schemas
│   ├── llm.py               # Groq LLM integration
│   ├── workflow_runner.py   # Workflow execution logic
│   ├── routes/              # API endpoints
│   │   ├── workflows.py
│   │   ├── runs.py
│   │   └── status.py
│   ├── templates/           # Jinja2 HTML templates
│   └── static/              # CSS and JavaScript
├── tests/                   # Test files
├── requirements.txt
├── .env.example
├── Dockerfile
└── README.md
```

## ✅ What's Implemented

- ✅ Create workflows with multiple steps
- ✅ Run workflows on input text
- ✅ View output for each step
- ✅ Run history (last 5)
- ✅ System status page with health checks
- ✅ Input validation
- ✅ Error handling
- ✅ Clean, modern UI
- ✅ Responsive design
- ✅ Sequential step chaining

## ❌ What's Not Implemented

- ❌ User authentication
- ❌ Workflow editing/deletion
- ❌ Custom step creation
- ❌ Export results to file
- ❌ Step reordering via drag-and-drop
- ❌ Advanced filtering/search

## 🚀 Deployment

### Render.com (Recommended)
1. Create new Web Service
2. Connect GitHub repo
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Add environment variable: `GROQ_API_KEY`

### Railway.app
1. Create new project from GitHub
2. Add `GROQ_API_KEY` environment variable
3. Deploy automatically

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/workflows/` | GET | List all workflows |
| `/api/workflows/` | POST | Create new workflow |
| `/api/workflows/{id}` | GET | Get workflow details |
| `/api/runs/` | POST | Execute workflow |
| `/api/runs/history` | GET | Get last 5 runs |
| `/api/runs/{id}` | GET | Get run details |
| `/api/status` | GET | System health check |

## 🧪 Testing

```bash
# Run basic health test
python -m pytest tests/

# Test API manually
curl http://localhost:8000/api/status
```

## 📝 License

MIT License - Feel free to use for learning and projects

## 👤 Author

Prasanna Nagarale - nagaraleprasanna@gmail.com

---

**Built with ❤️ using FastAPI and Groq**