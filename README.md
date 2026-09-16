# 🚀 FastAPI Authentication Service & Social Auth

A modern, fast, and scalable backend service built with **FastAPI** and **Python**. The project implements a complete user authentication lifecycle, JWT token management, OAuth2 (Social Auth) integration, and asynchronous database operations using **SQLAlchemy**.

---

## ✨ Key Features

- **Authentication & Authorization**: User registration, authentication, and secure password hashing (Bcrypt).
- **JWT (JSON Web Tokens)**: Generation and validation of Access and Refresh tokens for protected endpoints.
- **Social OAuth2**: Social login support via third-party providers (Google, GitHub).
- **Asynchronous ORM**: **SQLAlchemy** (AsyncIO) for high-performance database interaction.
- **Environment Management**: Fast dependency management using [`uv`](https://github.com/astral-sh/uv).
- **Interactive Documentation**: Automatically generated OpenAPI (Swagger UI / ReDoc) documentation.

---

## 🛠️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/) (Async)
- **Data Validation**: [Pydantic v2](https://docs.pydantic.dev/)
- **Package Manager**: [uv](https://docs.astral.sh/uv/)
- **Language**: Python 3.14

---

## 📁 Project Structure

```text
├── src/
│   └── app/
│       ├── api/            # API endpoints and routers
│       ├── core/           # Security, JWT, and global configuration
│       ├── models/         # SQLAlchemy database models
│       ├── Oauth2/         # Social Auth and OAuth2 provider integration
│       ├── repository/     # Database interaction layer (CRUD / Repository pattern)
│       ├── schemas/        # Pydantic schemas for data validation
│       ├── service/        # Business logic layer (Service layer)
│       ├── specification/  # Filtering and specification logic
│       ├── __init__.py     # Package initialization file
│       └── main.py         # Main FastAPI application entry point
├── .env                    # Environment variables configuration
├── .gitignore              # Files ignored by Git (.venv, .env, etc.)
├── LICENSE                 # Project license
├── pyproject.toml          # Project configuration and dependencies
├── README.md               # Project documentation
├── test.db                 # SQLite database file for local testing
└── uv.lock                 # Lockfile for uv package manager