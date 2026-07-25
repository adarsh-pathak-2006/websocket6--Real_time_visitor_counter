# Real-Time Visitor Counter

A modern, real-time visitor counter web application built with Django and Django Channels. It elegantly tracks and displays active connections using WebSockets, featuring a beautiful glassmorphism dark-mode UI.

## Features
- Real-time connection tracking using WebSockets (Django Channels)
- Stunning, responsive UI with glassmorphism design and micro-animations
- User authentication system (Login/Register)
- Deployment-ready with Redis channel layer support and WhiteNoise static files

## Getting Started

### Prerequisites
- Python 3.10+
- Redis (optional, but required for production)

### Installation
1. Clone the repository and navigate to the project directory:
   ```bash
   git clone <repository-url>
   cd counter
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Copy `.env.example` to `.env` and adjust the variables as needed.
   ```bash
   cp .env.example .env
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server (Uses ASGI/Daphne):
   ```bash
   python manage.py runserver
   ```

## Deployment
This project is configured to be production-ready:
- Ensure `DEBUG=False` in your `.env`.
- Set your domain in `ALLOWED_HOSTS`.
- Provide a `REDIS_URL` to use `RedisChannelLayer` for multi-worker support.
- Static files are served via `WhiteNoise`. Run `python manage.py collectstatic` before deployment.
- Use Daphne or an ASGI server (like Uvicorn/Gunicorn) to run the application in production.
