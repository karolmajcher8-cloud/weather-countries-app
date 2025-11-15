import mysql.connector

def mysql_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            database="weather_db",
            user="root",
            password="730334524"
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection, connection.cursor(dictionary=True)
    except mysql.connector.Error as e:
        print("Error while connecting to MySQL:", e)
        return None, None

def init_database():

    try:
        connection, cursor = mysql_connection()
        query = "CREATE DATABASE IF NOT EXISTS weather_db;"
        cursor.execute(query)

        print("Utworzono bazę")

        cursor.execute("USE weather_db;")

        print("Przełączono na bazę")

        create_table_query = """
        CREATE TABLE IF NOT EXISTS weather (
            id INT AUTO_INCREMENT PRIMARY KEY,
            temp FLOAT,
            feels_like FLOAT,
            humidity INT,
            pressure INT,
            wind_speed FLOAT,
            place VARCHAR(255),
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """

        cursor.execute(create_table_query)

        print("Tabela istnieje lub została utworzona")

    except Exception as e:
        print("Błąd przy tworzeniu tabeli lub bazy", e)

def insert_weather(data):
    try:
        connection, cursor = mysql_connection()

        query = """
        INSERT INTO weather 
        (temp,feels_like,humidity,pressure,wind_speed, place)
        VALUES 
        (%s, %s, %s, %s, %s, %s)
        """
        variables = (
            data["temp"], data["feels_like"], data["humidity"],
            data["pressure"], data["wind_speed"], data["place"]
        )

        cursor.execute(query, variables)

        connection.commit()

        print("Dodano nowy odczyt pogody")
        cursor.close()
        connection.close()

    except Exception as e:
        print(e)