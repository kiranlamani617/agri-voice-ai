#!/usr/bin/env python3
import socket
import sys
import os

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def check_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    sock.close()
    return result == 0

print("🌾 AgriVoice Server Status Check...")
print("-" * 45)
print(f"Port 3000 (Frontend Web UI): {'[OK] Running' if check_port(3000) else '[X] Not running'}")
print(f"Port 8000 (Backend API):     {'[OK] Running' if check_port(8000) else '[X] Not running'}")
print("-" * 45)

base_dir = os.path.dirname(os.path.abspath(__file__))
if not check_port(3000):
    print("\nFrontend not running! Start with:")
    print(f"  cd \"{os.path.join(base_dir, 'agrivoice-ui')}\"")
    print("  npm start")

if not check_port(8000):
    print("\nBackend not running! Start with:")
    print(f"  cd \"{os.path.join(base_dir, 'backend')}\"")
    print("  python manage.py runserver 0.0.0.0:8000")