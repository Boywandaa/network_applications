# HTTP Server & PyQt5 Web Browser

This project contains a simple asynchronous HTTP server built using Python's `asyncio`, and a custom web browser built with PyQt5. The server serves HTML pages, static assets, and handles basic form submissions. The browser is capable of rendering pages from the local server and provides a fallback option to search online (e.g., Google) when content is not found.

## Features

### HTTP Server (`server.py`)
- Asynchronous request handling using `asyncio`.
- Supports:
  - Static pages (HTML templates).
  - Form handling via POST requests.
  - Serving static assets like images.
- Custom response headers.
- Simple user registration system with file-based storage.

### PyQt5 Web Browser (`browser.py`)
- Connects to the local server (`http://localhost:8085`).
- Renders pages served by the HTTP server.
- Displays a custom "Page Not Found" page when a local resource doesn't exist.
- Provides a search bar to redirect to external search engines like Google.

---



