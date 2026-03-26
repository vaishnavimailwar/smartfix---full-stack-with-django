SmartFix — Vehicle Rescue Platform

A full-stack emergency vehicle rescue platform that connects stranded motorists with nearby mechanics in real time.

## 🚀 Project Overview

SmartFix is a web-based platform that allows users to request roadside assistance, track their assigned mechanic in real time, and get help fast. The platform includes a customer-facing rescue form, live GPS tracking, an admin dashboard, and a garage portal for mechanics.

## 🛠️ Tech Stack

| Layer      | Technology                        |
|------------|-----------------------------------|
| Frontend   | HTML, CSS, JavaScript             |
| Backend    | Django, Django REST Framework     |
| Database   | SQLite (Django default)           |
| Maps       | Leaflet.js + Google Maps Tiles    |
| Charts     | Chart.js                          |
| Auth       | Django Session Authentication     |
| Styling    | Custom CSS with CSS Variables     |
| Icons      | Google Material Symbols           |
| Fonts      | Bebas Neue, DM Sans, Space Mono   |

## 📁 Project Structure
```
smrt_fix/
├── backend/
│   ├── manage.py
│   ├── smartfix/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   └── api/
│       ├── models.py
│       ├── views.py
│       ├── serializers.py
│       ├── urls.py
│       └── admin.py
└── frontend/
    └── index.html
``
## ⚙️ Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/smrt_fix.git
cd smrt_fix
```
### 2. Set Up Backend
```bash
cd backend
pip install django djangorestframework django-cors-headers
python manage.py makemigrations
python manage.py migrate
```
### 3. Create Users
```bash
python manage.py shell
```
Paste this inside the shell:
```python
from django.contrib.auth.models import User

User.objects.create_superuser('smartfix', '', '678910')

for i in range(1, 5):
    User.objects.create_user(f'mechanic{i}', '', f'mechanic{i}@123')

print("All users created!")
exit()
```
### 4. Run the Backend Server
```bash
python manage.py runserver
```
Backend runs at: `http://127.0.0.1:8000`

### 5. Open Frontend
Open `frontend/index.html` in your browser directly.
Or serve it using VS Code Live Server at `http://127.0.0.1:5500`

## 🔐 Login Credentials

### Admin Panel
| Username  | Password |
|-----------|----------|
| smartfix  | 678910   |

### Garage Portal (Mechanics)
| Username   | Password       |
|------------|----------------|
| mechanic1  | mechanic1@123  |
| mechanic2  | mechanic2@123  |
| mechanic3  | mechanic3@123  |
| mechanic4  | mechanic4@123  |
---
## 🌐 API Endpoints

| Method | Endpoint                  | Description              |
|--------|---------------------------|--------------------------|
| POST   | /api/request/             | Submit new rescue request|
| GET    | /api/request/<id>/        | Get request by ID        |
| GET    | /api/requests/            | Get all requests         |
| POST   | /api/accept/<id>/         | Accept a request         |
| POST   | /api/auth/login/          | Login                    |
| POST   | /api/auth/logout/         | Logout                   |
---
## ✨ Features
### Customer Side
- Submit emergency rescue request with name, phone, vehicle details
- Auto GPS detection with live map pin
- Drag-to-adjust location pin on map
- Urgency level selection — Low / Medium / High
- Request ID generated instantly after submission
- Real-time mechanic tracking with ETA countdown
- Request journey timeline — Submitted → Accepted → En Route → Resolved

### Admin Panel
- Secured login — only one admin (smartfix)
- View all repair requests in tabular form
- Stats — Total requests, Accepted, High Urgency
- Charts — Status split (doughnut) + Urgency breakdown (bar)
- All requests auto-accepted on submission

### Garage Portal
- Secured login for 4 mechanics
- Shows logged-in mechanic name on entry
- View all active customer rescue requests
- Call customer directly from the card
- Navigate to customer location via Google Maps

### Track Page
- Enter Request ID to track status
- Accepts format: 7 or REQ7
- Shows live mechanic movement on map
- ETA countdown updates in real time
- Services & Pricing section
- Nearby Partner Garages list
---

## 🗺️ How It Works
Customer fills form
       ↓
Request saved in Django DB (auto-accepted)
       ↓
Request ID shown to customer (15 seconds)
       ↓
Customer enters ID in Track page
       ↓
Live mechanic tracking begins
       ↓
Mechanic arrives → Issue Resolved

## 🔧 Django Admin Panel

Access at: `http://127.0.0.1:8000/admin/`
Login with:
- Username: `smartfix`
- Password: `678910`

You can view, search, and filter all repair requests here.

## 📦 Dependencies

### Backend
```
django
djangorestframework
django-cors-headers
```

Install all:
```bash
pip install django djangorestframework django-cors-headers
```

### Frontend (CDN — no install needed)
- Leaflet.js `1.9.4`
- Chart.js `4.4.0`
- Google Fonts — Bebas Neue, DM Sans, Space Mono
- Google Material Symbols
- 
## 🚧 Known Limitations
- Frontend served as static HTML — not hosted on a server
- GPS tracking is simulated (mechanic movement is animated)
- SQLite used — not recommended for production
- No SMS or email notifications yet

## 🔮 Future Enhancements
- AI-based mechanic recommendation based on problem description
- Real mechanic GPS integration via mobile app
- SMS notification on request acceptance
- Payment gateway integration
- Progressive Web App (PWA) support
- Multi-language support (Kannada, Hindi, English)

## 👨‍💻 Developed By
**Team SmartFix**
1)Bhagyashree H K 
2)Harsh W
3)Shivani L R
4)Vaishnavi N M

Kalaburagi, Karnataka, India
Built as part of an enterprise-level full-stack project using Django + Vanilla JS.

---

## 📄 License

This project is for educational purposes.
All rights reserved © 2026 SmartFix.
