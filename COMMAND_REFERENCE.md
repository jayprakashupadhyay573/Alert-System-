# 📚 Command Reference Guide

## Quick Setup Commands

### Windows PowerShell

```powershell
# Complete setup in one go
python -m venv .venv; `
.venv\Scripts\Activate.ps1; `
pip install -r requirements.txt; `
python setup.py; `
uvicorn backend.main:app --reload --port 8000
```

### Windows Command Prompt

```cmd
REM Create virtual environment
python -m venv .venv
.venv\Scripts\activate.bat

REM Install dependencies
pip install -r requirements.txt

REM Run setup
python setup.py

REM Start server
uvicorn backend.main:app --reload --port 8000
```

### Mac / Linux

```bash
# Complete setup
python3 -m venv .venv && \
source .venv/bin/activate && \
pip install -r requirements.txt && \
python setup.py && \
uvicorn backend.main:app --reload --port 8000
```

---

## API Testing Commands

### Health & Status

```bash
# Health check
curl http://localhost:8000/health

# System status
curl http://localhost:8000/

# API overview
curl http://localhost:8000/api/v1/reports/overview
```

### User Management

```bash
# List all users
curl http://localhost:8000/api/v1/users

# Get specific user
curl http://localhost:8000/api/v1/users/IN001

# Load CSV data
curl -X POST http://localhost:8000/api/v1/users/load-csv

# Load specific CSV file
curl -X POST "http://localhost:8000/api/v1/users/load-csv?csv_filename=final_user_dataset_with_alert_stages.csv"

# Create new user
curl -X POST http://localhost:8000/api/v1/users \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "TEST001",
    "name": "Test User",
    "email": "test@example.com",
    "country": "India",
    "state": "Delhi",
    "role": "Student",
    "domain": "Engineering",
    "latitude": 28.7041,
    "longitude": 77.1025
  }'

# Update user
curl -X PUT http://localhost:8000/api/v1/users/IN001 \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Name"}'

# Delete user
curl -X DELETE http://localhost:8000/api/v1/users/IN001

# Delete all users (confirmation required)
curl -X DELETE "http://localhost:8000/api/v1/users?confirm=true"
```

### Analytics Endpoints

```bash
# Get overall analytics
curl http://localhost:8000/api/v1/analytics/overview

# Get all user analytics
curl http://localhost:8000/api/v1/analytics/users

# Get top 10 users
curl "http://localhost:8000/api/v1/analytics/top-users?limit=10"

# Get country-wise analytics
curl http://localhost:8000/api/v1/analytics/countries

# Get application-wise analytics
curl http://localhost:8000/api/v1/analytics/applications

# Get alert statistics
curl http://localhost:8000/api/v1/analytics/alerts
```

### Alert Management

```bash
# List all alerts
curl http://localhost:8000/api/v1/alerts

# Get alerts for specific user
curl http://localhost:8000/api/v1/alerts/IN001

# Evaluate alert for user
curl -X POST http://localhost:8000/api/v1/alerts/evaluate \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "IN001",
    "usage_minutes": 110
  }'

# Manually trigger alert
curl -X POST "http://localhost:8000/api/v1/alerts/trigger?user_id=IN001&stage=FINAL_ALERT"

# Delete specific alert
curl -X DELETE http://localhost:8000/api/v1/alerts/1
```

### ML Predictions

```bash
# Make prediction
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

# Train model from CSV
curl -X POST http://localhost:8000/api/v1/prediction/train-csv

# Get model status
curl http://localhost:8000/api/v1/prediction/model-status

# Get prediction for user
curl http://localhost:8000/api/v1/prediction/IN001

# Get all predictions
curl "http://localhost:8000/api/v1/prediction/results/all?limit=50"
```

### Reports

```bash
# System overview
curl http://localhost:8000/api/v1/reports/overview

# Alert flow diagram
curl http://localhost:8000/api/v1/reports/alert-flow

# Dataset information
curl http://localhost:8000/api/v1/reports/dataset-info

# Technology stack
curl http://localhost:8000/api/v1/reports/technology-stack
```

---

## Server Management

### Start Server

```bash
# Development (with auto-reload)
uvicorn backend.main:app --reload --port 8000

# Production (without reload)
uvicorn backend.main:app --host 0.0.0.0 --port 8000

# Multiple workers
uvicorn backend.main:app --workers 4 --host 0.0.0.0 --port 8000

# Custom host and port
uvicorn backend.main:app --host 127.0.0.1 --port 8001
```

### Database Management

```python
# Python console - Initialize database
python
>>> from backend.database import init_db
>>> init_db()
>>> exit()

# Python console - Load CSV data
python
>>> from backend.database import SessionLocal, init_db
>>> from backend.services.data_service import DataService
>>> init_db()
>>> db = SessionLocal()
>>> result = DataService.load_csv_data('final_user_dataset_with_alert_stages.csv', db)
>>> print(result)
>>> exit()

# Reset database (remove SQLite file)
rm alert_system.db  # Linux/Mac
del alert_system.db # Windows

# Check database creation
ls alert_system.db  # Linux/Mac
dir alert_system.db # Windows
```

### Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Activate (Windows CMD)
.venv\Scripts\activate.bat

# Activate (Mac/Linux)
source .venv/bin/activate

# Deactivate (all platforms)
deactivate

# Install requirements
pip install -r requirements.txt

# Upgrade pip
python -m pip install --upgrade pip

# Install specific package
pip install fastapi==0.104.1
```

---

## Browser Access

### Frontend Pages

| Page | URL | Purpose |
|------|-----|---------|
| Prediction Form | http://localhost:8000/index | Make predictions |
| Globe Visualization | http://localhost:8000/visualization | View globe and alerts |
| API Docs | http://localhost:8000/docs | Interactive Swagger UI |
| Alternative Docs | http://localhost:8000/redoc | ReDoc documentation |
| OpenAPI Schema | http://localhost:8000/openapi.json | OpenAPI specification |
| Health Check | http://localhost:8000/health | Server status |

---

## Development Commands

### Code Quality

```bash
# Run tests
pytest

# Run tests with async support
pytest -asyncio-mode=auto

# Lint with pylint
pylint backend/

# Format with black
black .

# Check types with mypy
mypy backend/
```

### Dependency Management

```bash
# Show installed packages
pip list

# Generate requirements from environment
pip freeze > requirements.txt

# Check for outdated packages
pip list --outdated

# Upgrade all packages
pip install --upgrade -r requirements.txt
```

---

## Debugging Commands

### Logging and Inspection

```bash
# Start server with debug logging
uvicorn backend.main:app --reload --log-level debug

# Check Python version
python --version

# List installed packages
pip list

# Find package location
pip show fastapi

# Check FastAPI version
python -c "import fastapi; print(fastapi.__version__)"
```

### Database Inspection

```python
# Python console - Check database tables
python
>>> from backend.database import SessionLocal, Base
>>> from backend.models import User, UsageRecord, Alert, PredictionResult
>>> db = SessionLocal()
>>> users = db.query(User).all()
>>> for user in users:
...     print(user)
>>> exit()

# Check database file info
ls -la alert_system.db  # Linux/Mac
dir alert_system.db     # Windows
```

---

## Environment Configuration

### Create .env File

```bash
# Copy template
cp .env.example .env

# Edit .env with your settings
# (On Windows use: copy .env.example .env)
```

### Common Environment Variables

```env
# Debug mode
DEBUG=True

# API configuration
API_V1_STR=/api/v1

# Database
DATABASE_URL=sqlite:///./alert_system.db
# DATABASE_URL=postgresql://user:password@localhost:5432/alert_db

# Alert thresholds
WARNING_THRESHOLD=100
FINAL_ALERT_THRESHOLD=120

# Email configuration (optional)
EMAIL_ADDRESS=your-email@gmail.com
EMAIL_APP_PASSWORD=your-app-password

# CORS origins
CORS_ORIGINS=["http://localhost", "http://localhost:8000"]

# WebSocket settings
WEBSOCKET_PING_INTERVAL=30

# ML Model paths
ML_MODEL_PATH=backend/ml/alert_model.pkl
ML_FEATURES_PATH=backend/ml/feature_names.pkl
ML_TARGET_ENCODER_PATH=backend/ml/target_encoder.pkl
ML_FEATURE_ENCODERS_PATH=backend/ml/feature_encoders.pkl
```

---

## Common Issues & Solutions

### Port Already in Use

```bash
# Use different port
uvicorn backend.main:app --reload --port 8001

# On Windows - find process using port
netstat -ano | findstr :8000

# On Mac/Linux - find process using port
lsof -i :8000
```

### Module Not Found Error

```bash
# Activate virtual environment
.venv\Scripts\Activate.ps1  # Windows
source .venv/bin/activate    # Mac/Linux

# Install requirements
pip install -r requirements.txt

# Verify installation
python -c "import backend; print('OK')"
```

### Database Lock

```bash
# Delete database file
rm alert_system.db  # Linux/Mac
del alert_system.db # Windows

# Re-initialize
python setup.py
```

### WebSocket Connection Failed

```bash
# Check if server is running
curl http://localhost:8000/health

# Check firewall settings
# Test WebSocket with wscat:
npm install -g wscat
wscat -c ws://localhost:8000/ws/alerts
```

---

## Performance Testing

### Load Testing

```bash
# Install Apache Bench
# Linux: sudo apt-get install apache2-utils
# Mac: brew install httpd
# Windows: Use ApacheBench for Windows

# Run load test (100 requests, 10 concurrent)
ab -n 100 -c 10 http://localhost:8000/health

# Run load test with POST
ab -n 100 -c 10 -p data.json -T application/json http://localhost:8000/api/v1/users
```

### Monitoring

```bash
# Watch directory for changes (Linux/Mac)
watch "curl http://localhost:8000/health"

# Continuous monitoring (Mac)
while true; do curl http://localhost:8000/health && sleep 2; done
```

---

## Deployment

### Docker Build & Run

```bash
# Build Docker image
docker build -t alert-system .

# Run Docker container
docker run -p 8000:8000 alert-system

# Run with environment file
docker run -p 8000:8000 --env-file .env alert-system

# Run with volume mount
docker run -p 8000:8000 -v $(pwd):/app alert-system
```

### Docker Compose

```bash
# Start services
docker-compose up

# Start in background
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f
```

---

## Useful Links

- FastAPI Docs: https://fastapi.tiangolo.com
- Uvicorn: https://www.uvicorn.org
- SQLAlchemy: https://docs.sqlalchemy.org
- Pydantic: https://docs.pydantic.dev
- Scikit-learn: https://scikit-learn.org/stable/documentation.html
- Three.js: https://threejs.org/docs/index.html

---

## Quick Troubleshooting Matrix

| Issue | Command to Try |
|-------|---|
| Server won't start | `uvicorn backend.main:app --reload --port 8001` |
| Module errors | `pip install -r requirements.txt` |
| Database issues | `rm alert_system.db && python setup.py` |
| Port in use | Check with `netstat` or use different port |
| WebSocket fails | Verify firewall, check `/docs` for connection info |
| No data in API | `curl -X POST http://localhost:8000/api/v1/users/load-csv` |
| Prediction fails | `curl http://localhost:8000/api/v1/prediction/model-status` |

---

**Bookmark this page for quick reference during development!** 🚀
