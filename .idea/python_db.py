import pyodbc

server = 'WIN-JFEREGV77LS'
database='TSQLV5'
driver= '{SQL Server Native Client 11.0}'

conn_str = (
      r"Driver="+driver+";"
      r"Server="+server+";"
      r"Database="+database+";"
      r"Trusted_Connection=yes"
)

# подключаемся к БД
conn = pyodbc.connect(conn_str)

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS students; CREATE TABLE students (first_name TEXT, last_name TEXT, age INTEGER);")

insert_query = "INSERT INTO students VALUES ('James', 'Brown', 21);"
cursor.execute(insert_query)

first_name = 'Jack'
last_name = 'White'
age = 22
insert_query = "INSERT INTO students VALUES (?, ?, ?);"
cursor.execute(insert_query, (first_name, last_name, age))

jane = ('Jane', 'Air', 18)
cursor.execute(insert_query, jane)

students = [
    ('Jane', 'Ostin', 19),
    ('Jack', 'Scott', 22),
    ('Bob', 'Green', 20)
]

for student in students:
    cursor.execute(insert_query, student)

cursor.executemany(insert_query, students)


# cursor.execute("SELECT * FROM students WHERE first_name IS 'James';")

# cursor.execute("UPDATE students SET last_name = 'Austen' WHERE last_name IS 'Ostin';")

# cursor.execute("DELETE FROM students WHERE last_name IS 'Green';")

# for row in cursor:
# 	print(row)

# print(cursor.fetchone())
# print(cursor.fetchall())

cursor.execute("SELECT * FROM students;")

data = cursor.fetchall()
[print(row) for row in data]

conn.commit()

conn.close()

# подключение к БД функцией
def save_eartquakes(place_magnitude_list):
    server = 'WIN-JFEREGV77LS'
    database='TSQLV5'
    driver= '{SQL Server Native Client 11.0}'

    conn_str = (
            r"Driver="+driver+";"
                              r"Server="+server+";"
                                                r"Database="+database+";"
                                                                      r"Trusted_Connection=yes"
    )

    # подключаемся к БД
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE earthquakes (place TEXT, magnitude REAL)")
    cursor.executemany("INSERT INTO earthquakes VALUES (?, ?)", place_magnitude_list)
    conn.commit()
    conn.close()


def select_all_earthquakes():
    server = 'WIN-JFEREGV77LS'
    database='TSQLV5'
    driver= '{SQL Server Native Client 11.0}'

    conn_str = (
        r"Driver="+driver+";"
        r"Server="+server+";"
        r"Database="+database+";"
        r"Trusted_Connection=yes"
    )

    # подключаемся к БД
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM earthquakes")
    data = cursor.fetchall()
    [print(row) for row in data]
    conn.commit()
    conn.close()






