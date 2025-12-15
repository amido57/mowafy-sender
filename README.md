# Mowafy Sender - Facebook Pages Messaging SaaS (MVP)

## Overview
A web-based SaaS application for managing and sending messages to Facebook Page conversations using official Meta APIs.

## Stack
- **Backend**: Python + Flask
- **Frontend**: React + Vite
- **Database**: SQLite / PostgreSQL
- **Hosting**: Railway

## Features (MVP)
- User authentication (Email)
- Facebook OAuth login
- Fetch Facebook Pages
- View Page Conversations
- Send manual messages
- Adjustable message delay
- Logs and status tracking

## Installation

### Backend
```bash
cd backend
pip install -r requirements.txt
flask run
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Database Setup
```bash
python
>>> from app import app
>>> from database import db
>>> with app.app_context():
...     db.create_all()
```

## Deployment
Deployed on Railway with PostgreSQL.

## Status
MVP in development. Phase 1 complete.
