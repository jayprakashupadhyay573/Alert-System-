# 🚀 Quick Start Guide

## One-Command Setup (Windows PowerShell)

```powershell
# 1. Create virtual environment
python -m venv .venv; .venv\Scripts\Activate.ps1; pip install -r requirements.txt

# 2. Run setup helper
python setup.py

# 3. Start FastAPI backend
uvicorn backend.main:app --reload --port 8000
```

## One-Command Setup (Mac/Linux)

```bash
# 1. Create virtual environment
python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt

# 2. Run setup helper
python setup.py

# 3. Start FastAPI backend
uvicorn backend.main:app --reload --port 8000
```

## Access Points

Once running, open these in your browser:

| Resource | URL |
|----------|-----|
| 🏠 Prediction Form | http://localhost:8000/index |
| 🌍 Globe Visualization | http://localhost:8000/visualization |
| 📚 API Docs (Swagger) | http://localhost:8000/docs |
| 📖 API Docs (ReDoc) | http://localhost:8000/redoc |
| 🏥 Health Check | http://localhost:8000/health |

## Load Sample Data

After starting the server, load the sample CSV data:

```bash
curl -X POST http://localhost:8000/api/v1/users/load-csv
```

## Make a Test Prediction

```bash
curl -X POST http://localhost:8000/api/v1/prediction/predict \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "IN001",
    "app_name": "WhatsApp",
    "country": "India",
    "state": "Delhi",
    "role": "Student",
    "domain": "Engineering",
    "usage_minutes": 110,
    "session_count": 5
  }'
```

## Verify Installation

```bash
# Test API health
curl http://localhost:8000/health

# Get system overview
curl http://localhost:8000/api/v1/reports/overview

# Get analytics
curl http://localhost:8000/api/v1/analytics/overview
```

## Common Issues & Solutions

**Issue: Port 8000 already in use**
```bash
# Use different port
uvicorn backend.main:app --reload --port 8001
```

**Issue: Module 'backend' not found**
```bash
# Ensure .venv is activated and requirements installed
.venv\Scripts\Activate.ps1  # Windows
python -m pip install -r requirements.txt
```

**Issue: Database locked**
```bash
# Reset database
rm alert_system.db
# Run setup again
python setup.py
```

**Issue: WebSocket connection failed**
- Check if backend is running on correct port
- Check browser console for error messages
- Verify CORS settings in backend/config.py

## Next Steps

1. ✅ Environment is set up
2. ✅ FastAPI backend is running
3. 📖 Read [README_FASTAPI.md](README_FASTAPI.md) for detailed documentation
4. 🤖 Train ML model: `curl -X POST http://localhost:8000/api/v1/prediction/train-csv`
5. 💾 Load sample data: `curl -X POST http://localhost:8000/api/v1/users/load-csv`
6. 🎨 Customize frontend in `templates/` and `static/`
7. 🚀 Deploy to production using Docker or cloud platform

## File Descriptions

| File | Purpose |
|------|---------|
| `backend/main.py` | FastAPI application entry point |
| `backend/config.py` | Configuration and settings |
| `backend/models.py` | SQLAlchemy database models |
| `backend/schemas.py` | Pydantic validation schemas |
| `backend/routers/` | API endpoint definitions |
| `backend/services/` | Business logic layer |
| `backend/websocket/` | WebSocket connection manager |
| `templates/index.html` | Prediction form page |
| `templates/visualization.html` | Globe visualization page |
| `static/style.css` | Form styling |
| `static/visualization.css` | Globe styling |
| `requirements.txt` | Python dependencies |
| `.env.example` | Environment configuration template |
| `setup.py` | Setup helper script |

## API Quick Reference

### Users
```bash
curl http://localhost:8000/api/v1/users                           # List users
curl http://localhost:8000/api/v1/users/{user_id}                 # Get user
curl -X POST http://localhost:8000/api/v1/users/load-csv           # Load CSV
```

### Analytics
```bash
curl http://localhost:8000/api/v1/analytics/overview               # Overview
curl http://localhost:8000/api/v1/analytics/users                  # All users
curl http://localhost:8000/api/v1/analytics/top-users              # Top users
curl http://localhost:8000/api/v1/analytics/countries              # By country
```

### Alerts
```bash
curl http://localhost:8000/api/v1/alerts                           # List alerts
curl http://localhost:8000/api/v1/alerts/{user_id}                 # User alerts
curl -X POST http://localhost:8000/api/v1/alerts/evaluate \
  -d '{"user_id":"IN001","usage_minutes":110}'                     # Evaluate
```

### Predictions
```bash
curl -X POST http://localhost:8000/api/v1/prediction/predict \
  -d '{...}'                                                        # Make prediction
curl http://localhost:8000/api/v1/prediction/model-status          # Model info
curl -X POST http://localhost:8000/api/v1/prediction/train-csv     # Train model
```

## Environment Variables

Key variables in `.env`:

```env
DEBUG=True                              # Debug mode
API_V1_STR=/api/v1                     # API base path
DATABASE_URL=sqlite:///./alert_system.db  # Database URL
WARNING_THRESHOLD=100                  # Minutes before warning
FINAL_ALERT_THRESHOLD=120              # Minutes before alert
```

## Support

- 📖 Full documentation: [README_FASTAPI.md](README_FASTAPI.md)
- 🐛 API issues: Check `/docs` endpoint
- 💬 Questions: Review code comments and docstrings

---

**Happy coding! 🎉**
