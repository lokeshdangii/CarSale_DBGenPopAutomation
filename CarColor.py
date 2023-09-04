import psycopg2

def create_car_color(db):
    cursor = db.cursor()

    # list of car colors
    car_colors = [
        (1, "White"),
        (2, "Black"),
        (3, "Silver"),
        (4, "Gray"),
        (5, "Red"),
        (6, "Blue"),
        (7, "Green"),
        (8, "Brown"),
        (9, "Yellow"),
        (10, "Orange")
    ]

    # create table query
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CarColor (
            ColorID SERIAL PRIMARY KEY,
            ColorName VARCHAR(50)
        )
    """)

    # insert query
    insert_query = "INSERT INTO CarColor (ColorID, ColorName) VALUES (%s, %s)"
    cursor.executemany(insert_query, car_colors)

    # commit the changes in database
    db.commit()
    cursor.close()

    print("CarColor table created and populated successfully.")
