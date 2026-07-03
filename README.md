# FastAPI Authentication & Authorization API

A RESTful authentication and authorization API built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **JWT**. This project demonstrates secure user authentication, password hashing with Argon2, role-based authorization, and protected endpoints.

---

## Features

- User registration
- User login
- JWT authentication
- Protected routes
- Current authenticated user endpoint (`/me`)
- Password reset
- Password hashing using Argon2
- PostgreSQL database
- SQLAlchemy ORM
- Pydantic request/response validation
- Environment variable configuration with `.env`

---

## Tech Stack

- Python 3.12+
- FastAPI
- PostgreSQL
- SQLAlchemy 2.x
- Pydantic v2
- Argon2
- python-jose (JWT)
- Uvicorn
- python-dotenv

---

## Project Structure

```text
app/
│
├── api/
│   ├── dependencies.py
│   └── routes/
│       ├── auth.py
│       ├── admin.py
│       ├── dashboard.py
│       └── url.py
│
├── core/
│   ├── database.py
│   └── security.py
│
├── models/
│   └── user.py
│
├── schemas/
│   ├── auth.py
│   └── user.py
│
├── main.py
│
create_db.py
requirements.txt
README.md
.env
```

---

## Installation

Clone the repository.

```bash
git clone <repository-url>
cd <project-folder>
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the virtual environment.

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
DB_KEY=postgresql+psycopg2://postgres:password@localhost:5432/credentials

SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Database

Create a PostgreSQL database.

Example:

```sql
CREATE DATABASE credentials;
```

Create the tables.

```bash
python create_db.py
```

---

## Running the Project

```bash
uvicorn app.main:app --reload
```

Server:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

## Authentication Flow

### Register

```
POST /api/v1/auth/register
```

Creates a new user account.

---

### Login

```
POST /api/v1/auth/login
```

Returns:

```json
{
    "access_token": "<jwt-token>",
    "token_type": "bearer"
}
```

---

### Authenticate Requests

Send the JWT using the Authorization header.

```
Authorization: Bearer <access_token>
```

---

### Current User

```
GET /api/v1/auth/me
```

Returns the authenticated user's information.

---

### Reset Password

```
PUT /api/v1/auth/reset-password
```

Requires authentication.

Request body:

```json
{
    "old_password": "currentPassword",
    "new_password": "newPassword"
}
```

---

## Security

This project follows common authentication practices:

- Passwords are hashed with Argon2.
- Plain-text passwords are never stored.
- JWT access tokens are used for authentication.
- Protected endpoints require a valid Bearer token.
- Password verification is performed before password updates.
- Environment variables are used for secrets and database credentials.

---

## Future Improvements

- Refresh tokens
- Email verification
- Forgot password workflow
- Role-Based Access Control (RBAC)
- User profile management
- Rate limiting
- Account lockout after repeated failed logins
- Docker support
- Unit and integration tests
- Alembic database migrations

---

## Learning Objectives

This project demonstrates:

- FastAPI fundamentals
- REST API development
- SQLAlchemy ORM
- PostgreSQL integration
- Authentication with JWT
- Authorization using dependencies
- Password hashing with Argon2
- Dependency Injection in FastAPI
- Secure backend development practices

---

## License

This project is intended for educational purposes and personal learning.
