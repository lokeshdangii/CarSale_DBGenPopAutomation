import psycopg2

def create_car_engine(db):
    cursor = db.cursor()

    # pre-defined engine names because faket do not generate engine names we want
    car_engines = [
        (1, "Gasoline"),
        (2, "Diesel"),
        (3, "Electric"),
        (4, "Hybrid")
    ]

    # create table query
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CarEngine (
            EngineID SERIAL PRIMARY KEY,
            EngineName VARCHAR(100)
        )
    """)

    # insert query
    insert_query = "INSERT INTO CarEngine (EngineID, EngineName) VALUES (%s, %s)"
    cursor.executemany(insert_query, car_engines)

    db.commit()
    cursor.close()

    print("CarEngine table created and populated successfully.")
