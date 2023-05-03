import psycopg2
import csv
 
connection = psycopg2.connect(dbname="postgres", user="postgres", password="494641", host="localhost")
cur = connection.cursor()
 
connection.autocommit = True
 
cur.execute("""CREATE TABLE IF NOT EXISTS PhoneBook 
(
    id SERIAL,
    surname VARCHAR(255),
    name VARCHAR(255),
    number INT
);
""")
 
while(True):
    print('Add data to the table:\n')
    print('Enter the values from console 1 or 0 to stop entering\n')
    a=int(input())
    if a==0:
        break
    print('Write first name: ')
    name=str(input())
    print('Write last name:\n')
    surname=str(input())
    print('Write a number:\n')
    number=int(input())
    cur.execute(f"INSERT INTO phonebook (surname, name, number) VALUES('{surname}', '{name}', '{number}')")
    connection.commit()
    print('###Data have been added!###\n')

while True:
    print("Do you want to insert data from csv file? Yes/No\n")
    mode=input()
    if mode=="no":
        break
    print('Enter the file name:\n')
    name=str(input())
    with open(name+'.csv', 'r') as f:
        read = csv.reader(f)
        for row in read:
            cur.execute("""
            INSERT INTO PhoneBook (surname, name, number) VALUES(%s, %s, %s)
            """, row)
            print(1)
    connection.commit()
    print('###Data have been added!###\n')

while True:
    print('Do you want to update data? Yes/No\n')
    mode=str(input())
    if mode =='No':
        break

    cur.execute('Select * FROM phonebook')
    query = cur.fetchall()

    for tuple in query:
        print(f"""
        --------------------
        id: {tuple[0]}
        Name: {tuple[1]}
        Surname: {tuple[2]}
        Number: {tuple[3]}
        --------------------
        """)

    print("Enter id")
    id=input()
    print('\nWhat do you want to change?')
    change = input()
    print('Enter new value')
    new_value = input()

    cur.execute(f"""
        UPDATE PhoneBook
        SET {change} = '{new_value}'
        WHERE id = {id}
    """)
    connection.commit()
    print('Updating...')

while True:
    print('Do you want to delete data? Yes/No\n')
    mode=input()
    if mode=='No':
        break
    cur.execute('Select * FROM phonebook')
    query = cur.fetchall()
    
    for tuple in query:
        print(f"""
        --------------------------------
                id: {tuple[0]}
                Name: {tuple[1]}
                Surname: {tuple[2]}
                Number: {tuple[3]}
        --------------------------------
        """)

    print("Enter id\n")
    id=input()
    cur.execute(f"""
    DELETE
    FROM PhoneBook
    WHERE id = {id}
    """)
    connection.commit()
    print('Deleting...')

while True:
    print('Do you want to get some data? Yes/No\n')
    mode=input()
    if mode=='No':
        break
    print('Enter about what do you want to get data? Name, Surname, Number, id\n')
    value = input()
    print('Enter data\n')
    value2 = input()
    cur.execute(f"""
    SELECT *
    FROM PhoneBook
    WHERE {value} = '{value2}'
    """)
    query = cur.fetchall()
    for tuple in query:
        print(f'''
        -----------------------------------
                id: {tuple[0]}
                Surname: {tuple[1]}
                Name: {tuple[2]}
                Number: {tuple[3]}
        -----------------------------------
        ''')

           
connection.commit()
cur.close()
connection.close()