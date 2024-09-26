import sqlite3

conn = sqlite3.connect('hw.db')
cursor = conn.cursor()


def show_cities():
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()

    print(
        "Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")

    for city in cities:
        print(f"{city[0]}. {city[1]}")

    return cities


def show_students(city_id):
    query = """
        SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
        FROM students
        JOIN cities ON students.city_id = cities.id
        JOIN countries ON cities.country_id = countries.id
        WHERE cities.id = ?
    """
    cursor.execute(query, (city_id,))
    students = cursor.fetchall()

    if students:
        for student in students:
            print(
                f"First name: {student[0]}; Last name: {student[1]}; Country: {student[2]}; City: {student[3]} Area: {student[4]} км²:")
    else:
        print("Нет учеников в этом городе.")

while True:


    cities = show_cities()

    try:
        city_id = int(input("\nВведите id города: "))
    except ValueError:
        print("Неверный ввод. Пожалуйста, введите число.")
        continue

    if city_id == 0:
        print("Вы вышли из программы.")
        break

    if any(city[0] == city_id for city in cities):
        show_students(city_id)
    else:
        print("Город с таким id не найден. Попробуйте еще раз.")

conn.close()

