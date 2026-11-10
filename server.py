#!/usr/bin/env python3
"""
Swasthya Connect - Local Development Server
Serves the web application and static JSON datasets.
"""

import http.server
import socketserver
import os
import sys

# Ensure UTF-8 console output on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Enable CORS and disable aggressive caching for live development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def run():
    os.chdir(DIRECTORY)
    
    # Try port 3000, fallback to 5173 or 8080 if in use
    port = PORT
    httpd = None
    for p in [3000, 5173, 8080, 8000]:
        try:
            httpd = socketserver.TCPServer(('', p), Handler)
            port = p
            break
        except OSError:
            continue

    if not httpd:
        print("Error: Could not bind to any test port (3000, 5173, 8080, 8000).")
        sys.exit(1)

    url = f"http://localhost:{port}"
    print("=" * 65)
    print("  Swasthya Connect - Community Healthcare Access Platform")
    print("  (Samudayik Arogya Manch)")
    print("=" * 65)
    print(f"  Local Server running at: {url}")
    print(f"  Serving directory:      {DIRECTORY}")
    print("  Press Ctrl+C to stop the server.")
    print("=" * 65)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()

if __name__ == '__main__':
    run()
