def convert_csv_to_sql(csv_file, db_config_or_engine):
    import pandas as pd
    import os
    from sqlalchemy import inspect
    from src.config import MySQLConnection

    table_name = os.path.basename(csv_file).split(".")[0]
    df = pd.read_csv(csv_file)

    # Allow dict or engine
    if isinstance(db_config_or_engine, dict):
        connection = MySQLConnection(**db_config_or_engine)
        engine = connection.get_engine()
    else:
        engine = db_config_or_engine

    inspector = inspect(engine)
    if table_name in inspector.get_table_names():
        raise ValueError(f"The Table '{table_name}' already exists.")

    if df.empty:
        raise ValueError("The CSV file is empty. Nothing to upload.")

    df.to_sql(name=table_name, con=engine, if_exists='fail', index=False)
    return table_name
