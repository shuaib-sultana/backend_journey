# User Management API (Flask + MySQL)

This project is a **User Management API** built with **Flask** and **MySQL**.  
The main purpose of this repository is to represent my **backend development journey**, starting from a clean and structured CRUD API and evolving into more advanced versions.

Future releases will include:
- JWT Authentication  
- Password Hashing  
- Middleware System  
- Logging System  
- Rate Limiting  
- Connection Pooling  
- Application Structure Improvements  
- Docker Support  

---

## 📌 Features (Current Version)
### ✔ CRUD Operations  
- Create user  
- Retrieve all users  
- Retrieve user by ID  
- Retrieve user by email  
- Update user  
- Delete user  

### ✔ Clean Architecture  
- `models/` → SQL queries  
- `services/` → Business logic  
- `routes/` → Flask Blueprints  
- `utils/` → Validators + response helpers  
- `core/` → Custom errors + error handler  
- `database/` → MySQL connection & query wrapper  

### ✔ Error Handling  
Custom exception system:
- `ValidationError`
- `NotFoundError`
- `AuthenticationError`
- `PermissionError`
- `DatabaseError`

All errors are returned in a consistent JSON format.

### ✔ Input Validation  
The API validates:
- Email format  
- Data types  
- Empty fields  
- Password length  
- JSON body structure  

---

## 📁 Project Structure
project/
|──app/
|  ├── core/
|  │ ├── error_handler.py
|  │ └── errors.py
|  │
|  ├── models/
|  │ └── user_model.py
|  │
|  ├── routes/
| │ └── user_routes.py
|  │
|  ├── services/
|  │ └── user_service.py
|  │
|  ├── utils/
|  │ ├── response.py
|  │ ├── validators.py
|  │ └── init.py
|  │
|  ├── config.py
|  ├── database.py
|  └── password.py ← (Not included in repository)
|──run.py


---

## 🚀 Running the Project

### 1) Create virtual environment
```bash
python -m venv venv
```
### 2) Activate it

Windows
```bash
venv\Scripts\activate
```

Linux/Mac
```bash
source venv/bin/activate
```
### 3) Install dependencies
```bash
pip install -r requirements.txt
```
### 4) Run the server
```bash
python run.py
```
## 🛢 Database Configuration

Database settings are located in:
```bash
app/config.py
```
For safety, the file:
```bash
app/password.py
``` 
>is ignored and **NOT nincluded** in the repository because it contains your database password.
---
## 🧩 API Endpoints
### GET /users

Retrieve all users.

### GET /user/id/<id>

Retrieve user by ID.

### GET /user/email/<email>

Retrieve user by email.

### POST /user/

Create new user.

### PUT /user/<id>

Update user.

### DELETE /user/<id>

Delete user.

---

## 📦 Future Versions

### This project will evolve into multiple advanced releases, including:

- Token-based authentication (JWT)

- Password hashing

- Role-based authorization

- Logging system

- Rate limiting

- Middleware engine

- Docker containerization
…and more.

---
## 📄 License

>This project is part of my backend training path and is open for learning & improvement.
