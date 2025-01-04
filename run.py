# run.py
from asgiref.wsgi import WsgiToAsgi
from app.api import app

# Wrap the Flask app for ASGI compatibility
asgi_app = WsgiToAsgi(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(asgi_app, host="0.0.0.0", port=8000)
