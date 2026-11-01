# Advanced Global User Analytics & Alert System

A comprehensive real-time global user monitoring and analytics system with machine learning-based alert predictions. Built with FastAPI, WebSockets, SQLAlchemy, and interactive 3D globe visualization using Three.js.

## 🎯 Project Overview

This project provides a complete solution for:
- **Real-time user activity tracking** across multiple countries
- **Intelligent alert system** with three stages (SAFE, WARNING, FINAL_ALERT)
- **3D globe visualization** with interactive user markers
- **Machine learning predictions** for alert stage classification
- **WebSocket real-time updates** for live data synchronization
- **Comprehensive analytics** and reporting capabilities

## ✨ Features

### Core Features
- ✅ User management and profiling
- ✅ Real-time usage tracking
- ✅ Multi-stage alert system with color-coded stages
- ✅ 3D interactive globe with user location markers
- ✅ FastAPI WebSocket for real-time updates
- ✅ ML-based alert predictions (Random Forest Classifier)
- ✅ Comprehensive analytics dashboard
- ✅ Email alert notifications
- ✅ Responsive design for desktop and mobile

### Alert System
- **SAFE** (Green/Cyan): Usage < 100 minutes - Normal operation
- **WARNING** (Orange/Yellow): Usage 100-120 minutes - High usage alert
- **FINAL_ALERT** (Red): Usage ≥ 120 minutes - Critical alert with sound and email

### Machine Learning
- Algorithm: Random Forest Classifier
- Predicts: Alert stage likelihood
- Features: country, state, role, domain, app_name, usage_minutes, session_count
- Model: Auto-trained from CSV data

## 🛠 Technology Stack

### Backend
- **Python 3.11+**
- **FastAPI** - Modern async web framework
- **Uvicorn** - ASGI server
- **SQLAlchemy** - ORM for database operations
- **Pydantic v2** - Data validation
- **Scikit-learn** - Machine learning
- **Pandas** - Data processing
- **Joblib** - Model persistence

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Responsive styling
- **JavaScript (ES6+)** - Modern scripting
- **Three.js** - 3D graphics library
- **WebSockets** - Real-time communication

### Database
- **SQLite** - Development
- **PostgreSQL** - Production-ready
- **MongoDB** - Alternative option

## 📁 Project Structure

```
Alert System/
├── backend/
│   ├── main.py                    # FastAPI application entry point
│   ├── config.py                  # Configuration settings
│   ├── database.py                # Database connection & session
│   ├── models.py                  # SQLAlchemy ORM models
│   ├── schemas.py                 # Pydantic validation schemas
│   │
│   ├── routers/
│   │   ├── users.py              # User management endpoints
│   │   ├── analytics.py          # Analytics endpoints
│   │   ├── alerts.py             # Alert management endpoints
│   │   ├── predictions.py        # ML prediction endpoints
│   │   └── reports.py            # System reports endpoints
│   │
│   ├── services/
│   │   ├── alert_service.py      # Alert logic & evaluation
│   │   ├── analytics_service.py  # Analytics aggregation
│   │   ├── data_service.py       # CSV data loading
│   │   └── prediction_service.py # ML model & predictions
│   │
│   ├── websocket/
│   │   └── manager.py            # WebSocket connection manager
│   │
│   ├── ml/
│   │   ├── alert_model.pkl       # Trained ML model
│   │   ├── feature_names.pkl     # Feature names
│   │   ├── target_encoder.pkl    # Target label encoder
│   │   └── feature_encoders.pkl  # Feature encoders
│   │
│   └── data/
│       └── (CSV datasets)
│
├── templates/
│   ├── index.html                 # Prediction form page
│   └── visualization.html         # Globe visualization page
│
├── static/
│   ├── style.css                 # Form styling
│   ├── visualization.css         # Globe styling
│   ├── visualization.js          # Original globe visualization
│   └── visualization_fastapi.js  # WebSocket-integrated visualization
│
├── app.py                        # Legacy Flask app (for reference)
├── train_model.py                # Model training script
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment configuration template
└── README.md                     # This file
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- Virtual environment support

### Step 1: Create Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

**Mac/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure Environment

Copy `.env.example` to `.env` and update settings:

```bash
cp .env.example .env
```

Edit `.env` with your configuration:
```env
DEBUG=True
API_V1_STR=/api/v1
DATABASE_URL=sqlite:///./alert_system.db
WARNING_THRESHOLD=100
FINAL_ALERT_THRESHOLD=120
```

### Step 4: Initialize Database

The database will be created automatically on first run. To pre-load CSV data:

```bash
# Option 1: Via API after starting server
curl -X POST http://localhost:8000/api/v1/users/load-csv

# Option 2: Manually from Python
python -c "
from backend.database import SessionLocal, init_db
from backend.services.data_service import DataService
init_db()
db = SessionLocal()
result = DataService.load_csv_data('final_user_dataset_with_alert_stages.csv', db)
print(result)
"
```

## 🏃 Running the Application

### Start FastAPI Backend

**Development (with hot reload):**
```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

**Production:**
```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --workers 4
```

The backend will be available at:
- API: `http://localhost:8000`
- API Docs (Swagger): `http://localhost:8000/docs`
- API Docs (ReDoc): `http://localhost:8000/redoc`
- WebSocket: `ws://localhost:8000/ws/alerts`

### Access Frontend

Open in browser:
- Prediction Form: `http://localhost:8000/index`
- Globe Visualization: `http://localhost:8000/visualization`

## 📚 API Documentation

### Authentication
Currently, no authentication is required. Configure as needed in production.

### Base URL
```
http://localhost:8000/api/v1
```

### Endpoints Overview

#### Users
- `GET /users` - List all users
- `GET /users/{user_id}` - Get specific user
- `POST /users` - Create new user
- `PUT /users/{user_id}` - Update user
- `DELETE /users/{user_id}` - Delete user
- `POST /users/load-csv` - Load data from CSV
- `DELETE /users?confirm=true` - Delete all users

#### Analytics
- `GET /analytics/overview` - Overall usage statistics
- `GET /analytics/users` - All users analytics
- `GET /analytics/top-users` - Top users by usage
- `GET /analytics/countries` - Country-wise analytics
- `GET /analytics/applications` - Application-wise analytics
- `GET /analytics/alerts` - Alert statistics

#### Alerts
- `GET /alerts` - List all alerts
- `GET /alerts/{user_id}` - Get user alerts
- `POST /alerts/evaluate` - Evaluate user alert stage
- `POST /alerts/trigger` - Manually trigger alert
- `DELETE /alerts/{alert_id}` - Delete alert record

#### Predictions
- `POST /prediction/predict` - Make prediction
- `POST /prediction/train-csv` - Train model from CSV
- `GET /prediction/{user_id}` - Get user prediction
- `GET /prediction/results/all` - All predictions
- `GET /prediction/model-status` - Model information

#### Reports
- `GET /reports/overview` - System overview
- `GET /reports/alert-flow` - Alert flow diagram
- `GET /reports/dataset-info` - Dataset information
- `GET /reports/technology-stack` - Tech stack info

### Example API Calls

**Get Analytics Overview:**
```bash
curl http://localhost:8000/api/v1/analytics/overview
```

**Make Prediction:**
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

**Load CSV Data:**
```bash
curl -X POST "http://localhost:8000/api/v1/users/load-csv?csv_filename=final_user_dataset_with_alert_stages.csv"
```

## 🔌 WebSocket Integration

### Connect to WebSocket
```javascript
const ws = new WebSocket('ws://localhost:8000/ws/alerts');

ws.onopen = () => {
    ws.send(JSON.stringify({
        action: 'subscribe',
        message: 'Connect to real-time updates'
    }));
};

ws.onmessage = (event) => {
    const message = JSON.parse(event.data);
    console.log('Update received:', message);
};
```

### Message Types
- `user_update` - User data changed
- `alert_triggered` - Alert status changed
- `usage_updated` - Usage time updated
- `pong` - Keep-alive response

## 🤖 Machine Learning

### Model Information
- **Algorithm:** Random Forest Classifier
- **Features:** 7 features (country, state, role, domain, app_name, usage_minutes, session_count)
- **Target:** Alert stage (SAFE, WARNING, FINAL_ALERT)
- **Model File:** `backend/ml/alert_model.pkl`

### Train Model

**From CSV File:**
```bash
curl -X POST http://localhost:8000/api/v1/prediction/train-csv \
  -H "Content-Type: application/json" \
  -d '{"csv_filename": "final_user_dataset_with_alert_stages.csv"}'
```

**From Uploaded File:**
```bash
curl -X POST http://localhost:8000/api/v1/prediction/train \
  -F "csv_file=@final_user_dataset_with_alert_stages.csv"
```

### Check Model Status
```bash
curl http://localhost:8000/api/v1/prediction/model-status
```

## 📊 Dataset Format

The CSV dataset should contain these columns:

| Column | Type | Description |
|--------|------|-------------|
| user_id | string | Unique user identifier (e.g., IN1, US1) |
| name | string | User's full name |
| email | string | User's email address |
| country | string | Country (India, US) |
| state | string | State/Region |
| role | string | User role (Student, Entrepreneur, Farmer) |
| domain | string | Domain/Field (Engineering, Medical, etc.) |
| app_name | string | Application being tracked |
| usage_time | integer | Usage time in minutes |
| session_count | integer | Number of sessions |
| avg_session_time | float | Average session duration |
| alert_stage | string | Current alert stage (SAFE, WARNING, FINAL_ALERT) |

Example row:
```
IN1,Rahul,rahul@email.com,India,Bihar,Student,Engineering,Flipkart,145,8,18,FINAL_ALERT
```

## 🎨 Frontend Integration

### Form Submission
The index.html form sends predictions to `/api/v1/prediction/predict` endpoint.

### Globe Visualization
The visualization.html integrates with:
- **WebSocket** for real-time updates
- **Analytics API** for dashboard data
- **Three.js** for 3D rendering

### CSS Styling
- `static/style.css` - Form and general styling
- `static/visualization.css` - Globe container and alert panel styling

## 🔧 Configuration

### Alert Thresholds
Edit in `.env`:
```env
WARNING_THRESHOLD=100        # Minutes before warning
FINAL_ALERT_THRESHOLD=120    # Minutes before critical alert
```

### Database Options

**SQLite (Default - Development):**
```env
DATABASE_URL=sqlite:///./alert_system.db
```

**PostgreSQL (Production):**
```env
DATABASE_URL=postgresql://user:password@localhost:5432/alert_db
```

**MongoDB:**
```env
MONGODB_URL=mongodb://localhost:27017/alert_db
```

### CORS Settings
Edit in `backend/config.py`:
```python
CORS_ORIGINS = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",  # Add your frontend URL
]
```

## 📋 Testing

### Health Check
```bash
curl http://localhost:8000/health
```

### List Users
```bash
curl http://localhost:8000/api/v1/users
```

### Get Analytics
```bash
curl http://localhost:8000/api/v1/analytics/overview
```

### WebSocket Test (using wscat or similar)
```bash
wscat -c ws://localhost:8000/ws/alerts
> {"action": "subscribe"}
```

## 🐛 Troubleshooting

### Database Lock Error
```bash
# Delete the database file to reset
rm alert_system.db
```

### Port Already in Use
```bash
# Use different port
uvicorn backend.main:app --port 8001
```

### Model Not Found
```bash
# Train model first
curl -X POST http://localhost:8000/api/v1/prediction/train-csv
```

### WebSocket Connection Failed
- Check firewall settings
- Verify backend is running
- Check browser console for errors

## 📈 Performance Optimization

### For Production
1. Use PostgreSQL instead of SQLite
2. Enable GZIP compression in Uvicorn
3. Use reverse proxy (Nginx)
4. Enable caching headers
5. Deploy in docker container

### Example Nginx Config
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }

    location /ws {
        proxy_pass http://127.0.0.1:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
    }
}
```

## 📝 API Response Examples

### Prediction Response
```json
{
    "success": true,
    "user_id": "IN001",
    "predicted_stage": "WARNING",
    "confidence": 0.85,
    "probabilities": {
        "SAFE": 0.1,
        "WARNING": 0.85,
        "FINAL_ALERT": 0.05
    },
    "current_usage": 110
}
```

### Analytics Response
```json
{
    "total_users": 150,
    "active_users": 120,
    "safe_users": 80,
    "warning_users": 25,
    "final_alert_users": 15,
    "average_usage": 85.5,
    "total_sessions": 1250,
    "max_usage": 180,
    "min_usage": 5
}
```

### WebSocket Alert Message
```json
{
    "type": "alert_triggered",
    "user_id": "IN001",
    "timestamp": "2024-08-28T10:30:45.123456",
    "alert": {
        "stage": "FINAL_ALERT",
        "message": "Usage limit exceeded",
        "usage": 125
    }
}
```

## 🔐 Security Considerations

### For Production
1. Add authentication (JWT, OAuth)
2. Use HTTPS/TLS
3. Implement rate limiting
4. Add request validation
5. Use environment secrets
6. Enable CORS only for trusted domains
7. Add input sanitization

Example JWT setup:
```python
from fastapi.security import HTTPBearer
from fastapi import Depends

security = HTTPBearer()

@app.get("/protected")
async def protected_route(credentials: HTTPAuthCredentialsBearer = Depends(security)):
    return {"message": "Authorized"}
```

## 📞 Support & Contribution

For issues or suggestions:
1. Check API documentation at `/docs`
2. Review error messages in console
3. Check database logs
4. Verify data format in CSV

## 📜 License

This project is provided as-is for educational and operational purposes.

## 🎓 Learning Resources

- **FastAPI Docs:** https://fastapi.tiangolo.com/
- **SQLAlchemy:** https://www.sqlalchemy.org/
- **Scikit-learn:** https://scikit-learn.org/
- **Three.js:** https://threejs.org/
- **WebSockets:** https://developer.mozilla.org/en-US/docs/Web/API/WebSocket

---

**Advanced Global User Analytics & Alert System v1.0.0**  
Built with ❤️ using FastAPI, WebSockets, and Machine Learning
