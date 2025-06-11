# 📁 CSV to MySQL Converter (CLI)
[![Python Tests](https://github.com/SidharthaManriquez44/csv_to_mysql/actions/workflows/python-app.yml/badge.svg)](https://github.com/SidharthaManriquez44/csv_to_mysql/actions/workflows/python-app.yml)
[![codecov](https://codecov.io/gh/SidharthaManriquez44/csv_to_mysql/graph/badge.svg?token=CJZE6LM7M5)](https://codecov.io/gh/SidharthaManriquez44/csv_to_mysql)

A simple and interactive Python CLI tool to upload `.csv` files into a MySQL database. Designed for fast ingestion, validation, and logging — ideal for data engineers, analysts, and backend developers.

## 🚀 Features

- Upload CSV files via interactive CLI
- Validates file existence, format, and content
- Converts and uploads to MySQL using SQLAlchemy
- Logs all events and errors (`logs/app.log`, `logs/error.log`)
- Environment-safe DB credentials via `.env`
- Modular and testable structure
- Clean, Pythonic code

## 🧱 Project Structure

```plaintext
csv_to_mysql/
├── cli/               # CLI interface
├── data/              # Test or imported CSV files
├── logs/              # Logs for info and errors
├── src/               # Core logic and configuration
├── tests/             # Unit tests
├── main.py            # Entry point
├── .env.example       # Example environment variables
├── .gitignore
├── README.md
└── requirements.txt
```

## ⚙️ Setup

1. **Clone this repository**

```bash
git clone https://github.com/SidharthaManriquez44/csv_to_mysql.git
cd csv_to_mysql
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

Using make:
```bash
make install
```
Or manually:

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

    Rename .env.example to .env and fill in your database credentials:

```plaintext
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=your_db
```
## 🧪 Run the App

```bash
python main.py
```
Follow the prompts in the terminal to upload your CSV file and connect to your MySQL database.


## 🧪 Run Tests (Optional)

```bash
pytest
```

## 🧹 Code Quality

   Lint, sort imports, and check types:
```bash
make lint
make format
make type-check
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## ✍️ Author
Developed by `Sidhartha Manriquez`.
Feel free to reach out or contribute to improve this project!
