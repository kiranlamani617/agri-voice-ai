#!/usr/bin/env python3
import subprocess
import os
import time
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(BASE_DIR, "backend")
FRONTEND_DIR = os.path.join(BASE_DIR, "agrivoice-ui")

def start_servers():
    print("🌾 Starting AgriVoice AI Application")
    print("=" * 55)
    
    backend_cmd = [sys.executable, "manage.py", "runserver", "0.0.0.0:8000"]
    frontend_cmd = "npm start"
    
    # Start backend
    print("\n[1/2] Starting Backend on http://localhost:8000...")
    print("=" * 30)
    backend_process = subprocess.Popen(
        backend_cmd,
        cwd=BACKEND_DIR,
        shell=True
    )
    
    time.sleep(2)
    
    # Start frontend
    print("\n[2/2] Starting Frontend on http://localhost:3000...")
    print("=" * 30)
    frontend_process = subprocess.Popen(
        frontend_cmd,
        cwd=FRONTEND_DIR,
        shell=True
    )
    
    print("\n" + "=" * 55)
    print("AgriVoice servers are online!")
    print("Frontend Web App: http://localhost:3000")
    print("Backend API:      http://localhost:8000")
    print("\nFarmers just speak -> get instant answers!")
    print("Press Ctrl+C to stop both servers")
    print("=" * 55)
    
    try:
        backend_process.wait()
        frontend_process.wait()
    except KeyboardInterrupt:
        print("\n\nStopping servers...")
        backend_process.terminate()
        frontend_process.terminate()
        print("Servers stopped.")

if __name__ == "__main__":
    start_servers()