# application.py

from app import create_app

# This is the WSGI application object
application = create_app()

if __name__ == "__main__":
    # Use app.run() only for local development; in production use Gunicorn or similar
    application.run(host="0.0.0.0", port=5001, debug=True)
