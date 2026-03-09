# HRMS Lite — Human Resource Management System

A lightweight, production-ready HRMS web application that enables basic employee management and daily attendance tracking. Built as a full-stack system with a REST API backend and designed for real-world usability.

---

## 🚀 Project Overview

HRMS Lite is an internal admin tool that allows:

### Employee Management

* Add new employees
* View employee list
* Delete employees
* Unique employee ID & email validation

### Attendance Management

* Mark daily attendance (Present / Absent)
* View employee attendance history
* One attendance record per employee per date

### Admin Panel

* Manage employees and attendance from Django Admin
* Search, filters, and list views

### Production Features

* RESTful API architecture
* MySQL database with persistent storage
* Dockerized services
* Server-side validation & error handling
* Health check endpoint
* Seed script for demo data

---

## 🧱 Tech Stack

### Backend

* Python
* Django
* Django REST Framework
* MySQL

### DevOps / Deployment

* Docker & Docker Compose
* Gunicorn (WSGI server)
* Render (Cloud deployment)

### Tools

* Postman (API testing)
* Django Admin

---

## 📦 System Architecture

Client → API Server → Database

* Django serves REST APIs
* Gunicorn runs the app server
* MySQL stores persistent data
* Docker manages containers

---

## ⚙️ Features Implemented

### ✅ Core Requirements

* Employee CRUD (Add, List, Delete)
* Attendance Marking
* Attendance Records per Employee
* Required field validation
* Email format validation
* Duplicate employee prevention
* Proper HTTP status codes
* Meaningful API error responses

### ✅ UI / Admin

* Professional Django admin interface
* Employee & Attendance management views

### ✅ Production Readiness

* Dockerized backend
* Environment-based configuration
* Static file handling
* Health endpoint: `/health/`
* MySQL persistent volume
* Seed data for demo

### ⭐ Bonus

* Attendance filtering (date/status/employee)
* Dashboard stats API

---

## 📁 Project Structure

```
hrms/
 ├─ core/                  # App logic
 │   ├─ models.py
 │   ├─ views.py
 │   ├─ serializers.py
 │   ├─ admin.py
 │   └─ management/commands/seed_data.py
 │
 ├─ hrms/                  # Project config
 │   ├─ settings.py
 │   ├─ urls.py
 │   └─ wsgi.py
 │
 ├─ Dockerfile
 ├─ docker-compose.yml
 ├─ docker-compose.prod.yml
 ├─ requirements.txt
 ├─ .env
 ├─ .env.prod
 └─ manage.py
```

---

## 🧪 API Endpoints

### Health

```
GET /health/
```

### Employees

```
GET    /api/employees/
POST   /api/employees/
DELETE /api/employees/{id}/
```

### Attendance

```
GET  /api/attendance/?employee_id=EMP001
POST /api/attendance/
GET  /api/attendance/?date=YYYY-MM-DD&status=Present
```

### Dashboard

```
GET /api/dashboard/
```

---

## 🛠️ Run Locally (Docker)

### 1. Clone Repository

```bash
git clone <repo-url>
cd hrms
```

### 2. Create Environment File

`.env`

```
DEBUG=1
SECRET_KEY=dev-secret
DB_NAME=hrms
DB_USER=hrms_user
DB_PASSWORD=hrms_pass
DB_HOST=db
DB_PORT=3306
```

### 3. Build & Start Containers

```bash
docker compose up --build
```

### 4. Run Migrations

```bash
docker compose exec web python manage.py migrate
```

### 5. Create Superuser

```bash
docker compose exec web python manage.py createsuperuser
```

### 6. Seed Demo Data (Optional)

```bash
docker compose exec web python manage.py seed_data
```

### 7. Access App

```
API:    http://localhost:8000
Admin:  http://localhost:8000/admin
Health: http://localhost:8000/health
```

---

## 🚀 Production Deployment

### Environment

* `DEBUG=0`
* Gunicorn server
* MySQL managed database
* Static files collected

### Steps

1. Push code to GitHub
2. Create Docker Web Service on Render
3. Add environment variables
4. Attach managed MySQL
5. Deploy

---

## 🧾 Assumptions & Limitations

* Single admin user (no authentication system)
* No payroll or leave management
* Basic attendance status only
* Designed for demo/internal usage

---

## 🔮 Future Improvements

* Authentication & role-based access
* Employee edit/update
* CSV export
* Monthly attendance reports
* Leave management
* Frontend dashboard UI

---

## 👤 Author

Vaibhav
