import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

# #sukursime lentele
# c.execute("""
#     CREATE TABLE people(
#         id INTEGER PRIMARY KEY,
#         name text,
#         age int)
#     """)
#
# names = [('1', 'Jonas', 34), ('2', 'Antanas', 35), ('3', 'Migle', 23)]
# c.executemany('INSERT INTO people VALUES (?, ?, ?)', names)
# c.execute('SELECT * FROM people')
#
# result = c.fetchall()
# for row in result:
#     print(row)


# c.execute("""
#     CREATE TABLE jobs (
#     id INTEGER PRIMARY KEY,
#     job_title text,
#     person_id INTEGER,
#     FOREIGN KEY(person_id) REFERENCES people (id))
#     """)
#
# jobs = [('1', 'Inzinierius', 1), ('2', 'Programuotojas', 2), ('3', 'Analitikas', 3)]
# c.executemany('INSERT INTO jobs VALUES (?,?,?)', jobs)

# c.execute(""" SELECT people.name, jobs.job_title from people
#             JOIN jobs on people.id = jobs.person_id
#             """)
#
# result = c.fetchall()
# print(result)

# c.execute("""
#     CREATE TABLE hobbies (
#     id INTEGER PRIMARY KEY,
#     hobby_title text,
#     person_id INTEGER,
#     FOREIGN KEY(person_id) REFERENCES people (id))
#     """)

hobbies = [('1', 'Zvejyba', 1), ('2', 'Knygu skaitymas', 2), ('3', 'Programavimas', 3)]
additional_hobbies = [('Begimas', '3'), ('Dainuoti', '3')]
c.executemany('INSERT INTO hobbies(hobby_title, person_id) VALUES (?, ?)', additional_hobbies)
c.execute(""" SELECT people.name, hobbies.hobby_title from people
            JOIN hobbies on people.id = hobbies.person_id WHERE people.name = 'Migle'
             """)

# MINDAUGO PVZZZ
# curs.execute("""
#     SELECT * FROM
#
#     (SELECT people.name as vardas, COUNT(hobbies.hobby) as hobiu_skaicius
#     FROM people
#     JOIN hobbies ON hobbies.person_id = people.id
#     GROUP BY people.id)
#
#     WHERE hobiu_skaicius > 1;
#     """)
# ans4 = curs.fetchall()
# print(ans4)

result = c.fetchall()
print(result)

# c.executemany('INSERT INTO hobbies VALUES (?,?,?)', hobbies)

# c.execute("""
#     UPDATE hobbies SET hobby = 'Programavimas' WHERE person_id = (SELECT id FROM people WHERE name = 'Migle')
#     and hobby = 'Begimas'
#     """)
#
# c.execute(""" SELECT people.name, hobbies.hobby_title from people
#             JOIN hobbies on people.id = hobbies.person_id
#             """)

# result = c.fetchall()
# print(result)

conn.commit()
conn.close()

# aaaaaa
