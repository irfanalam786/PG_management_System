import mysql.connector
from mysql.connector import Error

# Database connection details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '2004'
}

# SQL statements to create the database and tables
sql_statements = [
    "CREATE DATABASE IF NOT EXISTS management;",
    "USE management;",
    """
    CREATE TABLE IF NOT EXISTS customers (
      customer_ref INT NOT NULL AUTO_INCREMENT,
      name VARCHAR(45) NOT NULL,
      mother VARCHAR(45) NOT NULL,
      gender VARCHAR(45) NOT NULL,
      post VARCHAR(45) NOT NULL,
      mobile VARCHAR(45) NOT NULL,
      email VARCHAR(45) NOT NULL,
      nationality VARCHAR(45) NOT NULL,
      idproof VARCHAR(45) NOT NULL,
      idnumber VARCHAR(45) NOT NULL,
      address VARCHAR(45) NOT NULL,
      PRIMARY KEY (customer_ref)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS meal_plan (
      ID INT NOT NULL AUTO_INCREMENT,
      day VARCHAR(45) NOT NULL,
      meal_type ENUM('Veg','Non-Veg') NOT NULL,
      meal_details VARCHAR(255) NOT NULL,
      PRIMARY KEY (ID)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS room_details (
      customer_ref INT DEFAULT NULL,
      room_number INT NOT NULL,
      mobile VARCHAR(45) DEFAULT NULL,
      check_in DATE NOT NULL,
      duration ENUM('1 Month','2 Months','3 Months','6 Months','12 Months') NOT NULL,
      check_out DATE DEFAULT NULL,
      room_type ENUM('Single','Double','Suite') NOT NULL,
      meal_plan ENUM('None','Veg','Non-Veg') DEFAULT NULL,
      meal_price DECIMAL(10,2) DEFAULT NULL,
      total_price DECIMAL(10,2) DEFAULT NULL,
      PRIMARY KEY (room_number, check_in),
      KEY customer_ref (customer_ref),
      CONSTRAINT room_details_ibfk_1 FOREIGN KEY (customer_ref) REFERENCES customers (customer_ref) ON DELETE CASCADE
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS users (
      id INT NOT NULL AUTO_INCREMENT,
      email VARCHAR(255) NOT NULL,
      password VARCHAR(255) NOT NULL,
      security_question VARCHAR(255) NOT NULL,
      answer VARCHAR(255) NOT NULL,
      PRIMARY KEY (id)
    );
    """
]

# Meal plan data to be inserted
meal_plan_data = [
    ('Sunday', 'Veg', 'Veg Curry, Rice, Roti, Salad'),
    ('Sunday', 'Non-Veg', 'Chicken Curry, Rice, Roti, Salad'),
    ('Monday', 'Veg', 'Paneer Butter Masala, Rice, Roti, Salad'),
    ('Tuesday', 'Veg', 'Dal Tadka, Jeera Rice, Roti, Salad'),
    ('Wednesday', 'Veg', 'Mixed Veg, Rice, Roti, Salad'),
    ('Wednesday', 'Non-Veg', 'Mutton Curry, Rice, Roti, Salad'),
    ('Thursday', 'Veg', 'Chole Bhature, Salad'),
    ('Friday', 'Veg', 'Aloo Paratha, Curd, Salad'),
    ('Saturday', 'Veg', 'Vegetable Biryani, Raita, Salad')
]

# SQL statement to insert data
insert_query = """
INSERT INTO meal_plan (day, meal_type, meal_details) VALUES (%s, %s, %s);
"""

# Function to create the database and tables
def create_database_and_tables():
    connection = None
    try:
        connection = mysql.connector.connect(host=db_config['host'], user=db_config['user'], password=db_config['password'])
        if connection.is_connected():
            cursor = connection.cursor()
            for statement in sql_statements:
                cursor.execute(statement)
            print("Database and tables created successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Function to insert data into the meal_plan table
def insert_meal_plan_data():
    connection = None
    try:
        connection = mysql.connector.connect(**db_config, database='management')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.executemany(insert_query, meal_plan_data)
            connection.commit()
            print(f"{cursor.rowcount} rows inserted into meal_plan table.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Main execution
if __name__ == "__main__":
    create_database_and_tables()
    insert_meal_plan_data()
