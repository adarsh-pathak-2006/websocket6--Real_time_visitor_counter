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

## Deployment on Render
This project is configured to be seamlessly deployed on [Render](https://render.com). It uses ASGI (`daphne`) to serve Django Channels and includes a Redis instance for the channel layer.

### Deployment Steps
1. **Create a Redis Instance** on Render. Note down the **Internal Redis URL**.
2. **Create a Web Service**:
   - Environment: `Python 3`
   - Build Command: `./build.sh`
   - Start Command: `daphne counter.asgi:application --port $PORT --bind 0.0.0.0`
3. **Environment Variables**:
   - `PYTHON_VERSION`: `3.10.0`
   - `SECRET_KEY`: (Generate a secure random string)
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: `*` (or your Render URL)
   - `REDIS_URL`: (The Internal Redis URL from step 1)

*(Note: Don't forget to give execute permissions to your build script locally by running `chmod +x build.sh` before pushing to Git.)*
