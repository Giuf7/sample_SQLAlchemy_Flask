# Flask + SQLAlchemy — SQL Server Starter

A minimal project template demonstrating a clean DAL (Data Access Layer) architecture using **Flask**, **SQLAlchemy 2.0** and **SQL Server** via ODBC.

<img width="290" height="325" alt="image" src="https://github.com/user-attachments/assets/021a53f4-23ed-4276-b81e-23c4af3d900a" />

---

## Tech Stack

| Library       | Version |            Role              |
|---------------|---------|------------------------------|
| Flask         | 3.1.3   | Web framework / API          |
| SQLAlchemy    | 2.0.50  | ORM / database toolkit       |
| Pydantic      | 2.13.4  | Data validation              |
| python-dotenv | 1.2.2   | Environment variable loading |
| pyodbc        | 5.3.0   | SQL Server ODBC driver       |

---

## Project Structure

```
.
├── api/                # Flask
|   └──controllers
|   └──routes
|   └──schemas
│   └── app.py
├── dal/
│   ├── database.py     # Engine, session, init_db, seed_data
│   └── models/
│       ├── base.py     # SQLAlchemy DeclarativeBase
|   └── repositories/
├── .env                # Environment variables (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Getting Started

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the virtual environment

**Linux / macOS**
```bash
source .venv/bin/activate
```

**Windows**
```powershell
.\.venv\Scripts\Activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the database connection

Create a `.env` file at the project root (already listed in `.gitignore`):

```env
SERVER="YOUR_SERVER_NAME"
DATABASE="YOUR_DATABASE_NAME"

CONNECTION_STRING=mssql+pyodbc://@YOUR_SERVER_NAME/YOUR_DATABASE_NAME?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes&TrustServerCertificate=yes
```

> Windows Authentication is used by default (`trusted_connection=yes`).  
> Adjust the connection string if SQL Server authentication is required.

### 5. Initialize the database

```python
from dal.database import init_db, test_connexion

test_connexion()   # Verifies the connection
init_db()          # Creates all tables defined in models
```

---

## DAL Utilities

| Function                | Description                                |
|-------------------------|--------------------------------------------|
| `test_connexion()`      | Runs `SELECT 1` to verify connectivity     |
| `init_db(delete=False)` | Creates (or recreates) all tables          |
| `seed_data()`           | Inserts demo rows if the table is empty    |
| `get_db()`              | Context manager returning a scoped session |

---

## Requirements

- Python 3.10+
- SQL Server (local or remote)
- [ODBC Driver 17 for SQL Server](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server)
