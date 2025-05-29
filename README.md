# 📁 CSV to MySQL Converter (CLI)

A simple and interactive Python CLI tool to upload `.csv` files into a MySQL database. Designed for fast ingestion, validation, and logging — ideal for data engineers, analysts, and backend developers.

## 🚀 Features

- Upload CSV files via interactive CLI
- Validates file existence, format, and content
- Converts and uploads to MySQL using SQLAlchemy
- Logs all events and errors (`logs/app.log`, `logs/error.log`)
- Environment-safe DB credentials via `.env`
- Modular and testable structure
- Written with clean, Pythonic code

## 🧱 Project Structure

csv_to_mysql/
├── cli/ # CLI interface
├── data/ # Test or imported CSV files
├── logs/ # Logs for info and errors
├── src/ # Core logic and configuration
├── tests/ # Unit tests
├── main.py # Entry point
├── .env.example # Example environment variables
├── .gitignore
└── README.md


## ⚙️ Setup

1. **Clone this repository**

```bash
git clone https://github.com/SidharthaManriquez44/csv_to_mysql.git
cd csv_to_mysql
```

2. **Create a virtual environment**

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**
pip install -r requirements.txt

4. **Set up environment variables**

    Rename .env.example to .env and fill in your database credentials:

>DB_USER=your_user<br>
>DB_PASSWORD=your_password<br>
>DB_HOST=localhost<br>
>DB_PORT=3306<br>
>DB_NAME=your_db

## 🧪 Run the App

```bash
python main.py
```
Follow the prompts in the terminal to upload your CSV file and connect to your MySQL database.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## ✍️ Author
Developed by `Sidhartha Manriquez`.
Feel free to reach out or contribute to improve this project!