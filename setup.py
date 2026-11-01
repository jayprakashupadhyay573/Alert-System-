#!/usr/bin/env python
"""
Setup and initialization script for Advanced Global User Analytics & Alert System
"""
import os
import sys
from pathlib import Path

def main():
    print("=" * 70)
    print("Advanced Global User Analytics & Alert System - Setup Helper")
    print("=" * 70)
    
    # Check Python version
    if sys.version_info < (3, 11):
        print("❌ Python 3.11 or higher required!")
        sys.exit(1)
    
    print(f"✓ Python version: {sys.version.split()[0]}")
    
    # Check virtual environment
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  Virtual environment not detected")
        print("   Run: python -m venv .venv")
        print("   Then activate it before running this script")
    else:
        print("✓ Virtual environment detected")
    
    # Check dependencies
    try:
        import fastapi
        print("✓ FastAPI installed")
    except ImportError:
        print("❌ FastAPI not installed. Run: pip install -r requirements.txt")
        sys.exit(1)
    
    try:
        import sqlalchemy
        print("✓ SQLAlchemy installed")
    except ImportError:
        print("❌ SQLAlchemy not installed")
        sys.exit(1)
    
    try:
        import sklearn
        print("✓ Scikit-learn installed")
    except ImportError:
        print("❌ Scikit-learn not installed")
        sys.exit(1)
    
    # Initialize database
    print("\nInitializing database...")
    try:
        from backend.database import init_db
        init_db()
        print("✓ Database initialized")
    except Exception as e:
        print(f"❌ Error initializing database: {e}")
        sys.exit(1)
    
    # Check CSV file
    csv_file = "final_user_dataset_with_alert_stages.csv"
    if os.path.exists(csv_file):
        print(f"✓ Dataset file found: {csv_file}")
    else:
        print(f"⚠️  Dataset file not found: {csv_file}")
    
    # Check .env file
    if os.path.exists(".env"):
        print("✓ .env configuration file found")
    else:
        print("⚠️  .env file not found. Copying from .env.example...")
        if os.path.exists(".env.example"):
            import shutil
            shutil.copy(".env.example", ".env")
            print("✓ .env created from template")
        else:
            print("⚠️  .env.example not found")
    
    print("\n" + "=" * 70)
    print("Setup complete! Ready to run the application.")
    print("=" * 70)
    print("\n🚀 To start the FastAPI server, run:")
    print("   uvicorn backend.main:app --reload --port 8000")
    print("\n📚 API Documentation will be available at:")
    print("   http://localhost:8000/docs")
    print("\n📝 Access the application at:")
    print("   http://localhost:8000/index")
    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()
