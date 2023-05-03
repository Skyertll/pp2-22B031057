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
 
def data_console():
    print('Add data to the table:\n')
    print('Enter the values from console 1 or 0 to stop entering\n')
    a=int(input())
    if a==0:
        return
    print('Write first name: ')
    name=str(input())
    print('Write last name:\n')
    surname=str(input())
    print('Write a number:\n')
    number=int(input())
    cur.execute(f"INSERT INTO phonebook (surname, name, number) VALUES('{surname}', '{name}', '{number}')")
    connection.commit()
    print('###Data have been added!###\n')
    main()

def data_csv():
    print("Do you want to insert data from csv file? Yes/No\n")
    mode=input()
    if mode=="No":
        return
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
    main()

def update():
    print('Do you want to update data? Yes/No\n')
    mode=str(input())
    if mode =='No':
        main()

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
    main()

def exit():
    connection.commit()
    cur.close()
    connection.close()
    return

def delete():
    print('Do you want to delete data? Yes/No\n')
    mode=input()
    if mode=='No':
        main()
    cur.execute('Select * FROM phonebook')
    query = cur.fetchall()
    
    for tuple in query:
        print(f"""
        --------------------------------
                id: {tuple[0]}
                Name: {tuple[2]}
                Surname: {tuple[1]}
                Number: {tuple[3]}
        --------------------------------
        """)

    print("By what you want to delete data? 1=Name 2=Number\n")
    query_enter=int(input())
    if query_enter==1:
        print('Enter the name:')
        name_enter = input()
        cur.execute(f"""
        DELETE
        FROM PhoneBook
        WHERE "name" = '{name_enter}'
        """)
        connection.commit()
        print('Deleting...')
    if query_enter==2:
        print('Enter the phone number:')
        number = input()
        cur.execute(f"""
        DELETE
        FROM PhoneBook
        WHERE number = {number}
        """)
        connection.commit()
        print('Deleting...')
    main()



def query_pattern():
    list =[]
    print('''
    What do you want to search by?
    1. Name
    2. Surname
    3. Phone
    ''')
    b= int(input())
    if b==1:
        print('Enter pattern')
        pattern=input()
        cur.execute(f'''
        SELECT *
        FROM PhoneBook
        WHERE name LIKE '{pattern}'
        ''')
        for i in cur.fetchall():
            if len(i)!=0:
                if i not in list:
                    list.append(i)

        cur.execute(f'''
        SELECT *
        FROM PhoneBook
        WHERE name LIKE '{pattern}%'
        ''')
        for i in cur.fetchall():
            if len(i)!=0:
                if i not in list:
                    list.append(i)

        cur.execute(f'''
        SELECT *
        FROM PhoneBook
        WHERE name LIKE '%{pattern}'
        ''')
        for i in cur.fetchall():
            if len(i)!=0:
                if i not in list:
                    list.append(i)

        cur.execute(f'''
        SELECT *
        FROM PhoneBook
        WHERE name LIKE '%{pattern}%'
        ''')
        for i in cur.fetchall():
            if len(i)!=0:
                if i not in list:
                    list.append(i)
    if b==2:
        print('Enter pattern')
        pattern=input()
        cur.execute(f'''
        SELECT *
        FROM PhoneBook
        WHERE surname LIKE '{pattern}'
        ''')
        for i in cur.fetchall():
            if len(i)!=0:
                if i not in list:
                    list.append(i)

        cur.execute(f'''
        SELECT *
        FROM PhoneBook
        WHERE surname LIKE '{pattern}%'
        ''')
        for i in cur.fetchall():
            if len(i)!=0:
                if i not in list:
                    list.append(i)

        cur.execute(f'''
        SELECT *
        FROM PhoneBook
        WHERE surname LIKE '%{pattern}'
        ''')
        for i in cur.fetchall():
            if len(i)!=0:
                if i not in list:
                    list.append(i)

        cur.execute(f'''
        SELECT *
        FROM PhoneBook
        WHERE surname LIKE '%{pattern}%'
        ''')
        for i in cur.fetchall():
            if len(i)!=0:
                if i not in list:
                    list.append(i)
    if b==3:
        print('Enter pattern')
        pattern=input()
        cur.execute(f'''
        SELECT *
        FROM PhoneBook
        WHERE CAST(number as VARCHAR) LIKE '{pattern}'
        ''')
        for i in cur.fetchall():
            if len(i)!=0:
                if i not in list:
                    list.append(i)

        cur.execute(f'''
        SELECT *
        FROM PhoneBook
        WHERE CAST(number as VARCHAR) LIKE '{pattern}%'
        ''')
        for i in cur.fetchall():
            if len(i)!=0:
                if i not in list:
                    list.append(i)

        cur.execute(f'''
        SELECT *
        FROM PhoneBook
        WHERE CAST(number as VARCHAR) LIKE '%{pattern}'
        ''')
        for i in cur.fetchall():
            if len(i)!=0:
                if i not in list:
                    list.append(i)

        cur.execute(f'''
        SELECT *
        FROM PhoneBook
        WHERE CAST(number as VARCHAR) LIKE '%{pattern}%'
        ''')
        for i in cur.fetchall():
            if len(i)!=0:
                if i not in list:
                    list.append(i)
    for tuple in list:
        print(f'''
        -----------------------------------
                id: {tuple[0]}
                Surname: {tuple[1]}
                Name: {tuple[2]}
                Number: {tuple[3]}
        -----------------------------------
        ''')
    main()

def query():
    print('Do you want to get some data? Yes/No\n')
    mode=input()
    if mode=='No':
        main()
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
    main()

def name_phone():
    print('Enter name: ')
    name=input()
    print('Enter number: ')
    number = int(input())
    cur.execute(f'''
    SELECT count(*)
    FROM PhoneBook
    WHERE number = '{number}' AND name= '{name}'
    ''')
    if cur.fetchone()[0] == 0:
        cur.execute(f'''
        INSERT INTO PhoneBook (name, number)
        VALUES ({name}, {number})
        ''')
    else:
        cur.execute(f'''
        UPDATE PhoneBook
        SET number = {number}
        WHERE name = '{name}'
        ''')
    main()

def list_users():
    correct = []
    incorrect=[]
    print('Enter in order surname, name and phone or enter 0 to stop inserting')
    while True:
        enter = input().split()
        print(enter)
        if enter[0] == '0':
            break
        if not enter[2].isdigit():
            incorrect.append(enter)
            continue
        cur.execute(f'''
        INSERT INTO PhoneBook (surname, name, number)
        VALUES ('{enter[0]}', '{enter[1]}', {enter[2]})
        ''')
    if len(incorrect)==0:
        main()
    print('Incorrect data:')
    for i in incorrect:
        print(i)
    connection.commit()
    main()

def pagination():
    print('Enter the name:')
    name = input()
    print('Enter the limit')
    limit = int(input())
    print('Enter the offset')
    offset = int(input())
    cur.execute(f'''
    SELECT *
    FROM PhoneBook
    WHERE "name" = '{name}'
    LIMIT {limit}
    OFFSET {offset}
    ''')
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
    main()

def main():
    print('''
    ---------------------
    What do you want to do?
    1. Add data to the table
    2. Insert data from csv file
    3. Update data
    4. Delete data
    5. Get some data
    6. Get data with some pattern
    7. Insert user by name and phone
    8. Insert users by list of name and phone
    9. Pagination
    10. Exit
    ---------------------
    ''')
    a= int(input())
    functions = [data_console, data_csv, update, delete, query, query_pattern, name_phone, list_users, pagination]
    functions[a + 1]()
main()