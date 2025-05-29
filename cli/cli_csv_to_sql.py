import shutil
import os
from src.converter.csv_to_sql import convert_csv_to_sql
from src.logger import logger
from datetime import datetime


db_config = {}

def run_cli():
    while True:
        print("\n📋 Menu: CSV to MySQL Converter")
        print("1. Upload CSV file")
        print("2. Config your MySQL variables")
        print("3. Close")

        choice = input("Select an option: ")

        if choice == "1":
            csv_file = input("🗂️ Enter the absolute path of the CSV file: ").strip()

            if not os.path.exists(csv_file):
                logger.warning("🚫 File not found.")
                print("❌ The file does not exist. Try again.")
                continue
            if not csv_file.lower().endswith(".csv"):
                logger.warning("🚫 The file is not a CSV. Please try again.")
                continue
            # Copy file to data folder
            filename = os.path.basename(csv_file)
            dest_path = os.path.join("data", filename)
            try:
                shutil.copy(csv_file, dest_path)
                logger.info(f"✅ File copied to 'data/{filename}'")

                if not db_config:
                    logger.warning("⚠️ Please configure the MySQL connection first (option 2).")
                    continue
                confirm = input("Do you want to continue uploading to MySQL? (y/n): ")
                if confirm.lower() != 'y':
                    continue
                # Convert to MySQL using db_config if available
                try:
                    table_name = convert_csv_to_sql(dest_path, db_config)
                    logger.info(f"Table '{table_name}' successfully created '{filename}' at {datetime.now()}")
                    print(f"✅ Tabla '{table_name}' successfully created in MySQL.")

                except ValueError as ve:
                    logger.warning(f"⚠️ Validation error: {ve}")
                    print(f"⚠️ {ve}")
                except Exception as e:
                    logger.error(f"❌ Error converting CSV to MySQL: {e}")
                    print("❌ Failed to upload to MySQL. See error.log for details.")


            except Exception as e:
                print("❌ An error occurred copying the file. See error.log for details.")
                logger.error(f"❌ Error upload the CSV to MySQL: {e}")
                continue

        elif choice == "2":
            db_config["user"] = input("Provide your DB username: ").strip()
            db_config["password"] = input("Provide your DB password: ").strip()
            db_config["host"] = input("Provide the Host: ").strip()
            db_config["port"] = input("Provide the Port: ").strip()
            db_config["db_name"] = input("Provide your DB Name: ").strip()
            print("✅ Database configuration saved!")
            try:
                if not all(db_config.values()):
                    raise ValueError("All fields are required to configure MySQL.")
                logger.info("✅ MySQL configuration updated successfully.")
            except ValueError as ve:
                logger.warning(f"⚠️ {ve}")
                print(f"⚠️ {ve}")


        elif choice == "3":
            print("👋 See you later!")
            break

        else:
            logger.error("❌ Invalid option. Try again.")
            print("❌ Invalid option. Try again.")
