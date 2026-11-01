# Advanced Global User Analytics & Alert System

A comprehensive **real-time global user monitoring and analytics system** with machine learning-based alert predictions. Built with **FastAPI**, **WebSockets**, and interactive **3D globe visualization**.

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- pip package manager

### Installation (30 seconds)

```bash
# 1. Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Mac/Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run FastAPI backend
uvicorn backend.main:app --reload --port 8000
```

### Access the Application

Open in your browser:
- **Prediction Form:** http://localhost:8000/index
- **Globe Visualization:** http://localhost:8000/visualization  
- **API Docs:** http://localhost:8000/docs
- **Alternative Docs:** http://localhost:8000/redoc

## ✨ Key Features

✅ **Real-time Alert System** - Three-stage alerts (SAFE, WARNING, FINAL_ALERT)  
✅ **3D Globe Visualization** - Interactive user location markers  
✅ **WebSocket Updates** - Live real-time data synchronization  
✅ **Machine Learning** - Random Forest predictions for alert classification  
✅ **Analytics Dashboard** - Comprehensive user and usage analytics  
✅ **RESTful API** - Complete backend with Swagger documentation  
✅ **Responsive Design** - Works on desktop, tablet, and mobile  
✅ **Database Agnostic** - SQLite (dev), PostgreSQL (production)  

## 📚 Complete Documentation

For detailed information, see **[README_FASTAPI.md](README_FASTAPI.md)** which includes:

- 📖 Full project structure and architecture
- 🔌 API endpoints and WebSocket integration
- 🤖 Machine learning model information
- 🛠️ Configuration and environment setup
- 📊 Database schema and data formats
- 🔧 Production deployment guidelines
- 🧪 Testing and troubleshooting

## 🎯 System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      Frontend (HTML/JS)                          │
│          ┌────────────────────────────────────┐                 │
│          │ • Prediction Form (index.html)     │                 │
│          │ • 3D Globe Visualization           │                 │
│          │ • Alert Panel & Dashboard          │                 │
│          └────────────────────────────────────┘                 │
└──────────────────────────────────────────────────────────────────┘
                              ↕️ (REST API + WebSocket)
┌──────────────────────────────────────────────────────────────────┐
│                    FastAPI Backend (Python)                       │
│   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│   │ Users API    │  │ Analytics    │  │ Alerts API   │           │
│   └──────────────┘  └──────────────┘  └──────────────┘           │
│   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│   │ Predictions  │  │ Reports      │  │ WebSocket    │           │
│   └──────────────┘  └──────────────┘  └──────────────┘           │
│                                                                   │
│   Services Layer:                                               │
│   ┌────────────────────────────────────────────────────────┐   │
│   │ Alert Logic │ Analytics │ ML Predictions │ Data Load  │   │
│   └────────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────┘
                              ↕️
┌──────────────────────────────────────────────────────────────────┐
│                      SQLite Database                              │
│         (Users | Usage Records | Alerts | Predictions)          │
└──────────────────────────────────────────────────────────────────┘
```

## ⚡ Alert Stages

| Stage | Color | Threshold | Action |
|-------|-------|-----------|--------|
| 🟢 **SAFE** | Green/Cyan | < 100 min | No action |
| 🟠 **WARNING** | Orange/Yellow | 100-120 min | Display warning |
| 🔴 **FINAL_ALERT** | Red | ≥ 120 min | Sound + Email + Visual Effect |

## 📊 Example API Response

**Get Analytics Overview:**
```bash
curl http://localhost:8000/api/v1/analytics/overview
```

Response:
```json
{
    "total_users": 150,
    "active_users": 120,
    "safe_users": 80,
    "warning_users": 25,
    "final_alert_users": 15,
    "average_usage": 85.5,
    "total_sessions": 1250
}
```

**Make a Prediction:**
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

## 🔌 WebSocket Real-time Updates

```javascript
// Connect to WebSocket
const ws = new WebSocket('ws://localhost:8000/ws/alerts');

// Subscribe to updates
ws.send(JSON.stringify({ action: 'subscribe' }));

// Receive real-time alerts
ws.onmessage = (event) => {
    const message = JSON.parse(event.data);
    if (message.type === 'alert_triggered') {
        console.log('Alert:', message.alert);
    }
};
```

## 🤖 Machine Learning

The system automatically trains a **Random Forest Classifier** to predict alert stages based on:
- User country and state
- User role and domain
- Application name
- Current usage time
- Session count

Train the model:
```bash
curl -X POST http://localhost:8000/api/v1/prediction/train-csv
```

## 📁 Project Structure

```
Alert System/
├── backend/                      # FastAPI backend
│   ├── main.py                  # Application entry point
│   ├── config.py                # Configuration
│   ├── models.py                # Database models
│   ├── schemas.py               # Data validation
│   ├── routers/                 # API endpoints
│   ├── services/                # Business logic
│   └── websocket/               # Real-time updates
├── templates/                   # HTML templates
├── static/                      # CSS & JavaScript
├── requirements.txt             # Python dependencies
└── README_FASTAPI.md           # Complete documentation
```

## 🔧 Environment Configuration

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Edit configuration as needed:
```env
DEBUG=True
DATABASE_URL=sqlite:///./alert_system.db
WARNING_THRESHOLD=100
FINAL_ALERT_THRESHOLD=120
```

## 🧪 Testing

**Health Check:**
```bash
curl http://localhost:8000/health
```

**Load CSV Data:**
```bash
curl -X POST http://localhost:8000/api/v1/users/load-csv
```

**Get Top Users:**
```bash
curl http://localhost:8000/api/v1/analytics/top-users
```

## 🔐 API Documentation

Interactive API documentation available at:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc
- **OpenAPI JSON:** http://localhost:8000/openapi.json

## 📦 Technology Stack

| Component | Technology |
|-----------|-----------|
| Backend | FastAPI, Python 3.11+ |
| Server | Uvicorn (ASGI) |
| Database | SQLAlchemy ORM with SQLite |
| Data | Pandas, NumPy |
| ML | Scikit-learn (Random Forest) |
| Frontend | HTML5, CSS3, JavaScript, Three.js |
| Real-time | WebSockets |
| Validation | Pydantic v2 |

## 🚀 Production Deployment

See [README_FASTAPI.md](README_FASTAPI.md) for:
- Docker containerization
- Nginx reverse proxy setup
- PostgreSQL configuration
- Performance optimization
- Security hardening

## ❓ Troubleshooting

**Port already in use:**
```bash
uvicorn backend.main:app --port 8001
```

**Database issues:**
```bash
rm alert_system.db  # Reset database
```

**Model not found:**
```bash
# Train model from CSV data
curl -X POST http://localhost:8000/api/v1/prediction/train-csv
```

## 📞 Common Commands

```bash
# Activate virtual environment
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run backend
uvicorn backend.main:app --reload

# Run with specific port
uvicorn backend.main:app --port 8001

# Load CSV data
curl -X POST http://localhost:8000/api/v1/users/load-csv

# Get system status
curl http://localhost:8000/health
```

## 📖 For More Information

👉 See **[README_FASTAPI.md](README_FASTAPI.md)** for comprehensive documentation including:
- Complete API reference
- WebSocket integration guide
- ML model training
- Database configuration
- Deployment instructions
- Performance tuning
- Security best practices

---

**Advanced Global User Analytics & Alert System v1.0.0**  
FastAPI-based real-time monitoring with ML predictions
