from cli.cli_csv_to_sql import run_cli
from src.logger import logger

if __name__ == "__main__":
    try:
        run_cli()
    except KeyboardInterrupt:
        logger.info("🛑 User interrupted the program.")
        print("\n🛑 Program terminated by user.")
    except Exception as e:
        logger.error(f"Unhandled error in CLI: {e}")
        print("❌ A critical error occurred. See error.log for details.")
