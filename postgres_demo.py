import psycopg2

def execute_command(command: str):
    conn = psycopg2.connect(database='studentdb',user='postgres',password='admin123',host='localhost',port='5432')
    cur = conn.cursor()
    cur.execute(command)
    conn.commit()
    conn.close()

def create_table():
    execute_command('create table students(student_id serial primary key,name text,address text,age int,phone text);')

def insert_data():
    name = input('Enter name: ')
    address = input('Enter address: ')
    age = input('Enter age: ')
    phone = input('Enter phone: ')
    execute_command(f"insert into students(name,address,age,phone) values ('{name}','{address}','{age}','{phone}');")

def update_data():
    student_id = input("Enter Id of the student to be updated: ")
    fields = {
        '1': ('name', 'Enter the new name: '),
        '2': ('address','Enter the new address: '),
        '3': ('age','Enter the new age: '),
        '4': ('phone','Enter the new phone: ')
    }
    print('Which field would you like to update')
    for key in fields:
        print(f"{key}:{fields[key][0]}")
    choice = input('Enter number you want to update')
    if choice in fields:
        field_name, prompt = fields[choice]
        new_value = input(prompt)
        sql = f"update students set {field_name}='{new_value}' where student_id={student_id};"
        execute_command(sql)
        print(f"{field_name} updated successfully")
    else:
        print('Invalid choice')

def delete_data():
    student_id = input("Enter Id of the student to be deleted: ")
    conn = psycopg2.connect(database='studentdb',user='postgres',password='admin123',host='localhost',port='5432')
    cur = conn.cursor()
    cur.execute(f"select * from students where student_id='{student_id}';")
    student_row = cur.fetchone()
    if student_row is not None:
        cur.execute(f"delete from students where student_id={student_id};")
        conn.commit()
    else:
        print('There is no such id')
    conn.close()

insert_data()
update_data()
delete_data()