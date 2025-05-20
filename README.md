# Public Health Job Search Platform

This is a Flask-based web application that scrapes and displays job listings in Public Health, Epidemiology, Biostatistics, and Global Health.

## Features
- Web scraping of job listings
- Search and filter by keyword and location
- Interactive sortable table with DataTables.js
- Google Analytics tracking
- Local comment system stored in SQLite
- Visitor IP logging
- Dockerized deployment
- One-click deploy on Render

## Deployment on Render
1. Push this repo to GitHub
2. Go to [Render](https://render.com)
3. Click “New Web Service” and connect your GitHub repo
4. Select:
   - Runtime: **Docker**
   - Branch: **main**
   - Leave build/start commands blank
5. Click “Create Web Service”

Render will build your Docker image, run the `init_db.py` script, and start the Flask app.

## Run Locally
```bash
python init_db.py
python app/app.py
```
