# 📑 Project File Index

## 📚 Documentation Files (Start Here!)

| File | Purpose | Read Time |
|------|---------|-----------|
| **README.md** | Quick start guide and project overview | 5 min |
| **QUICKSTART.md** | One-command setup instructions | 3 min |
| **README_FASTAPI.md** | Complete technical documentation | 30 min |
| **IMPLEMENTATION_SUMMARY.md** | What was built and why | 15 min |
| **COMMAND_REFERENCE.md** | All commands and API examples | 10 min |
| **FILE_INDEX.md** | This file - project structure overview | 5 min |

**Recommended Reading Order:**
1. Start: README.md
2. Quick setup: QUICKSTART.md
3. Reference: COMMAND_REFERENCE.md
4. Deep dive: README_FASTAPI.md
5. Summary: IMPLEMENTATION_SUMMARY.md

---

## 🖥️ Backend Application Files

### Core Application
```
backend/
├── main.py                  # FastAPI application entry point (400 lines)
│                             # - CORS configuration
│                             # - Static files mounting
│                             # - Router registration
│                             # - WebSocket endpoint
│                             # - Health checks
│                             # - Startup/shutdown events
│
├── config.py               # Configuration management (50 lines)
│                            # - Settings class using Pydantic
│                            # - Database URL
│                            # - Alert thresholds
│                            # - ML model paths
│                            # - WebSocket configuration
│
├── database.py             # Database setup (40 lines)
│                            # - SQLAlchemy engine creation
│                            # - Session factory
│                            # - Base class for models
│                            # - Dependency for getting DB sessions
│
├── models.py               # SQLAlchemy ORM Models (150 lines)
│                            # - User model
│                            # - UsageRecord model
│                            # - Alert model
│                            # - PredictionResult model
│                            # - AlertStage enum
│
└── schemas.py              # Pydantic validation schemas (250 lines)
                             # - UserCreate, UserUpdate, UserResponse
                             # - UsageRecordCreate, UsageRecordResponse
                             # - AlertCreate, AlertResponse
                             # - PredictionRequest, PredictionResponse
                             # - Analytics schemas
                             # - WebSocket message schema
```

### API Routers
```
backend/routers/
├── users.py                # User management endpoints (120 lines)
│                            # GET /users - list all
│                            # GET /users/{id} - get one
│                            # POST /users - create
│                            # PUT /users/{id} - update
│                            # DELETE /users/{id} - delete
│                            # POST /users/load-csv - load from CSV
│                            # DELETE /users - delete all
│
├── analytics.py            # Analytics endpoints (100 lines)
│                            # GET /analytics/overview
│                            # GET /analytics/users
│                            # GET /analytics/top-users
│                            # GET /analytics/countries
│                            # GET /analytics/applications
│                            # GET /analytics/alerts
│
├── alerts.py               # Alert management (150 lines)
│                            # GET /alerts - list
│                            # GET /alerts/{user_id} - user alerts
│                            # POST /alerts/evaluate - evaluate stage
│                            # POST /alerts/trigger - manually trigger
│                            # DELETE /alerts/{id} - delete
│
├── predictions.py          # ML predictions (150 lines)
│                            # POST /prediction/predict
│                            # POST /prediction/train-csv
│                            # POST /prediction/train (upload)
│                            # GET /prediction/{user_id}
│                            # GET /prediction/results/all
│                            # GET /prediction/model-status
│
└── reports.py              # System reports (200 lines)
                             # GET /reports/overview
                             # GET /reports/alert-flow
                             # GET /reports/dataset-info
                             # GET /reports/technology-stack
```

### Services (Business Logic)
```
backend/services/
├── alert_service.py        # Alert evaluation logic (100 lines)
│                            # - evaluate_alert_stage()
│                            # - get_alert_message()
│                            # - should_trigger_email_alert()
│                            # - get_alert_color()
│                            # - get_alert_sound()
│                            # - update_threshold()
│
├── analytics_service.py    # Data aggregation (150 lines)
│                            # - get_usage_analytics()
│                            # - get_user_analytics_list()
│                            # - get_country_analytics()
│                            # - get_application_analytics()
│                            # - get_top_users()
│                            # - get_alert_stats()
│
├── data_service.py         # CSV loading (200 lines)
│                            # - load_csv_data()
│                            # - _get_latitude()
│                            # - _get_longitude()
│                            # - clear_all_data()
│
└── prediction_service.py   # ML model & predictions (250 lines)
                             # - load_model()
                             # - predict()
                             # - prepare_features()
                             # - train_model_from_csv()
```

### WebSocket Management
```
backend/websocket/
└── manager.py              # WebSocket connection manager (150 lines)
                             # - connect()
                             # - disconnect()
                             # - broadcast()
                             # - send_personal_message()
                             # - broadcast_user_update()
                             # - broadcast_alert()
                             # - broadcast_usage_update()
```

### Package Init Files
```
backend/
├── __init__.py             # Package marker (empty)
├── routers/__init__.py     # Routers package marker
├── services/__init__.py    # Services package marker
├── websocket/__init__.py   # WebSocket package marker
└── ml/                     # ML directory
    ├── __init__.py         # Package marker
    ├── alert_model.pkl     # Trained Random Forest model
    ├── feature_names.pkl   # Feature names list
    ├── target_encoder.pkl  # Target label encoder
    └── feature_encoders.pkl # Feature value encoders
```

---

## 🎨 Frontend Files

### HTML Templates
```
templates/
├── index.html              # Prediction form page (200 lines)
│                            # - Country/state/role selectors
│                            # - Usage input fields
│                            # - Form submission (fetch API)
│                            # - Result display
│                            # - Auto-location detection
│
└── visualization.html      # Globe visualization page (80 lines)
                             # - 3D globe container
                             # - Alert panel
                             # - Prediction pipeline display
                             # - Location marker
```

### JavaScript
```
static/
├── visualization.js        # Original globe visualization (200 lines)
│                            # - Three.js scene setup
│                            # - Earth, grid, atmosphere meshes
│                            # - Network visualization
│                            # - Animation loop
│
└── visualization_fastapi.js # WebSocket-enabled version (350 lines)
                              # - Connection manager
                              # - Auto-reconnect logic
                              # - Message handlers
                              # - Sound alerts
                              # - Notification system
```

### CSS Styling
```
static/
├── style.css               # Form styling (150 lines)
│                            # - Container layout
│                            # - Form input styling
│                            # - Button styling
│                            # - Result box styling
│                            # - Responsive design
│
└── visualization.css       # Globe styling (300 lines)
                             # - Dashboard grid layout
                             # - Panel styling
                             # - Globe container
                             # - Alert panel
                             # - Prediction flow
                             # - Animation effects
```

---

## ⚙️ Configuration & Utility Files

### Configuration
```
.env                         # Environment variables (generated from template)
│                            # - Database URL
│                            # - Alert thresholds
│                            # - Email settings
│                            # - API settings
│
.env.example                 # Configuration template
│                            # - Copy to .env before running
│                            # - Update with your settings
│
requirements.txt            # Python package dependencies (27 lines)
│                            # - FastAPI 0.104.1
│                            # - SQLAlchemy 2.0.23
│                            # - Scikit-learn 1.8.0
│                            # - Pandas 2.2.0
│                            # - Pydantic 2.5.0
│                            # - And 7 more packages
```

### Scripts
```
setup.py                     # Automated setup helper (100 lines)
│                            # - Python version check
│                            # - Virtual environment detection
│                            # - Dependency verification
│                            # - Database initialization
│                            # - File existence checks
```

### Legacy Files (Reference)
```
app.py                       # Original Flask application
│                            # - Kept for reference
│                            # - Now superseded by FastAPI backend
│
train_model.py              # Model training script
│                            # - Kept for reference
│                            # - Now integrated into API
```

---

## 📊 Data Files

### Dataset
```
final_user_dataset_with_alert_stages.csv  # Training dataset (~100+ rows)
│                                          # - user_id
│                                          # - name
│                                          # - country, state
│                                          # - role, domain
│                                          # - app, usage_time
│                                          # - session_count
│                                          # - alert_stage
│
```

### Database
```
alert_system.db              # SQLite database (auto-created)
│                            # - Created on first run
│                            # - Contains:
│                            #   - users table
│                            #   - usage_records table
│                            #   - alerts table
│                            #   - prediction_results table
```

### Pickle Files (ML Models)
```
alert_model.pkl              # Trained Random Forest model
feature_names.pkl            # List of feature names
target_encoder.pkl           # Label encoder for target
feature_encoders.pkl         # Encoders for features
```

---

## 📁 Complete Project Structure

```
Alert System/
├── backend/                          # FastAPI backend package
│   ├── main.py                      # Application entry point
│   ├── config.py                    # Configuration
│   ├── database.py                  # Database setup
│   ├── models.py                    # ORM models
│   ├── schemas.py                   # Pydantic schemas
│   ├── __init__.py                  # Package marker
│   │
│   ├── routers/                     # API endpoint modules
│   │   ├── users.py
│   │   ├── analytics.py
│   │   ├── alerts.py
│   │   ├── predictions.py
│   │   ├── reports.py
│   │   └── __init__.py
│   │
│   ├── services/                    # Business logic modules
│   │   ├── alert_service.py
│   │   ├── analytics_service.py
│   │   ├── data_service.py
│   │   ├── prediction_service.py
│   │   └── __init__.py
│   │
│   ├── websocket/                   # Real-time communication
│   │   ├── manager.py
│   │   └── __init__.py
│   │
│   └── ml/                          # Machine learning directory
│       ├── alert_model.pkl          # Trained model
│       ├── feature_names.pkl        # Feature list
│       ├── target_encoder.pkl       # Target encoder
│       ├── feature_encoders.pkl     # Feature encoders
│       └── __init__.py
│
├── templates/                        # HTML templates
│   ├── index.html                   # Prediction form
│   └── visualization.html           # Globe visualization
│
├── static/                          # Static assets
│   ├── style.css                    # Form styling
│   ├── visualization.css            # Globe styling
│   ├── visualization.js             # Original globe script
│   └── visualization_fastapi.js     # WebSocket-enabled script
│
├── Documentation (Start Here!)
│   ├── README.md                    # Quick start guide
│   ├── README_FASTAPI.md            # Complete documentation
│   ├── QUICKSTART.md                # One-command setup
│   ├── COMMAND_REFERENCE.md         # Commands and examples
│   ├── IMPLEMENTATION_SUMMARY.md    # What was built
│   └── FILE_INDEX.md                # This file
│
├── Configuration & Setup
│   ├── .env                         # Environment variables
│   ├── .env.example                 # Configuration template
│   ├── requirements.txt             # Python dependencies
│   ├── setup.py                     # Setup helper script
│   └── .gitignore                   # Git ignore rules
│
├── Data Files
│   ├── final_user_dataset_with_alert_stages.csv
│   ├── alert_system.db              # Auto-created database
│   ├── alert_model.pkl              # Saved ML model
│   ├── feature_names.pkl            # Model features
│   └── target_encoder.pkl           # Target encoder
│
└── Legacy Reference
    ├── app.py                       # Original Flask app
    └── train_model.py               # Original training script
```

---

## 🎯 File Size & Complexity

| Component | Files | Lines | Complexity |
|-----------|-------|-------|-----------|
| Backend Core | 5 | 1,000+ | High |
| API Routers | 5 | 800+ | Medium |
| Services | 4 | 800+ | High |
| WebSocket | 1 | 150+ | Medium |
| Frontend | 4 | 700+ | Medium |
| Configuration | 3 | 200+ | Low |
| Documentation | 6 | 2,000+ | Low |
| **Total** | **28+** | **5,650+** | **Medium** |

---

## 🔑 Key Files to Know

### Must Read First
1. **README.md** - Project overview and quick start
2. **QUICKSTART.md** - Get running in 3 commands

### For Development
3. **backend/main.py** - Application entry point
4. **backend/routers/** - API endpoints
5. **backend/services/** - Business logic
6. **templates/index.html** - Frontend form

### For Understanding
7. **README_FASTAPI.md** - Complete technical guide
8. **COMMAND_REFERENCE.md** - All available commands
9. **IMPLEMENTATION_SUMMARY.md** - What was built

### For Configuration
10. **.env.example** - Configuration template
11. **requirements.txt** - Package dependencies

---

## 📈 How to Navigate

### I want to...

**...get started quickly**
→ Read README.md then QUICKSTART.md

**...understand the architecture**
→ Read README_FASTAPI.md (Structure section)

**...use the API**
→ Read COMMAND_REFERENCE.md or visit /docs when server is running

**...fix an issue**
→ Check COMMAND_REFERENCE.md troubleshooting section

**...deploy to production**
→ Read README_FASTAPI.md (Deployment section)

**...add new features**
→ Study backend/routers/ and backend/services/ structure

**...understand ML predictions**
→ Read backend/services/prediction_service.py

**...modify the frontend**
→ Edit templates/index.html and static/style.css

**...track an issue**
→ Check IMPLEMENTATION_SUMMARY.md

---

## 📞 Quick Help

| Question | Answer File |
|----------|-------------|
| How do I start? | README.md |
| What's the command to run? | QUICKSTART.md or COMMAND_REFERENCE.md |
| What API endpoints exist? | COMMAND_REFERENCE.md or visit /docs |
| How does the system work? | README_FASTAPI.md or IMPLEMENTATION_SUMMARY.md |
| What was changed from Flask? | IMPLEMENTATION_SUMMARY.md |
| I'm stuck on something | COMMAND_REFERENCE.md (Troubleshooting) |
| Can I see code examples? | COMMAND_REFERENCE.md (API Examples) |
| What's the project structure? | This file (FILE_INDEX.md) |

---

## ✅ Verification Checklist

After setup, verify these files exist:

- [ ] `backend/main.py` - Main application
- [ ] `backend/routers/` - Contains 5 router files
- [ ] `backend/services/` - Contains 4 service files
- [ ] `templates/index.html` - Frontend form
- [ ] `static/style.css` - Styling
- [ ] `requirements.txt` - Dependencies listed
- [ ] `.env.example` - Configuration template
- [ ] `README.md` - Main documentation
- [ ] `README_FASTAPI.md` - Full documentation
- [ ] `alert_system.db` - Database (auto-created)

---

## 🎓 Learning Path

1. **Getting Started** (5 minutes)
   - Read: README.md
   - Do: Run `QUICKSTART.md` commands

2. **Understanding Basics** (15 minutes)
   - Read: `COMMAND_REFERENCE.md`
   - Do: Try a few API calls
   - Visit: http://localhost:8000/docs

3. **Going Deeper** (30 minutes)
   - Read: `README_FASTAPI.md`
   - Explore: Backend structure
   - Try: Load data and make predictions

4. **Advanced Topics** (1+ hours)
   - Read: `IMPLEMENTATION_SUMMARY.md`
   - Study: Code in `backend/services/`
   - Modify: Frontend in `templates/`

5. **Production Ready** (depends)
   - Deploy: Follow deployment section in README_FASTAPI.md
   - Scale: Configure database and caching
   - Monitor: Set up logging and alerts

---

**Welcome to the Advanced Global User Analytics & Alert System!** 🚀

This file index should help you navigate the project structure. Start with README.md and enjoy exploring!
