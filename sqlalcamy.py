from sqlalchemy import Table,Column,MetaData,String,Integer
from sqlalchemy import create_engine

engine = create_engine('sqlite:///college.db',echo=True)
meta=MetaData()

students=Table('students',meta,
Column('id',Integer,primary_key=True),
Column('name',String),
Column('lastname',String))

meta.create_all(engine)

def add():
    T = int(input('How many queries you want insert- '))
    for _ in range(T):
        name=input('Enter the name - ')
        lastname=input('Enter the lastname- ')
        conn = engine.connect()
        conn.execute(students.insert(),[{'name':name,'lastname':lastname}])

def display():
    list1=[]
    s = students.select()
    conn = engine.connect()
    result = conn.execute(s)
    for i in result:
        list1.append(i)
    if len(list1)<=0:
        print('Table is null! please add data')
        print('-'*50)
        print('Add the data- ')
        return add()
    else:
        print(list1)



def update():
    try:
        conn=engine.connect()
        ask=input('what you want to change[name/lastname]- ')
        if ask.lower()=='name':
            old_name=input('Enter the name you want to change- ')
            new_name=input('Enter the new name- ')
            strt=students.update().where(students.c.name==old_name).values(name=new_name)
            conn.execute(strt)
            s=students.select()
            conn.execute(s).fetchall()
        elif ask.lower()=='lastname':
            old_name=input('Enter the lastname you want to change- ')
            new_name=input('Enter the new lastname- ')
            strt=students.update().where(students.c.lastname==old_name).values(lastname=new_name)
            conn.execute(strt)
            s=students.select()
            conn.execute(s).fetchall()
    except:
        Exception(f'Error! wrong input{ask} is not present in table')
        return update()


def delete():
    try:
        name=input('Enter the name you want to delete- ')
        conn=engine.connect()
        stmt = students.delete().where(students.c.name==name)
        conn.execute(stmt)
        s=students.select()
        conn.execute(s).fetchall()
    except:
        raise Exception('Wrong Input! data not found')

def ask_():
    print('-'*90)
    op=input('You want to do operations -[Yes/No]- ')
    print('-'*90)

    if op.lower()=='yes':
        ask=input('What you want to do - 1)Add 2) Display 3)Update 4)Delete ')
        if ask=='display'.lower():
            display()
            print()
        elif ask=='update'.lower():
            update()
            display()
            ask_()
        elif ask=='delete'.lower():
            delete()
            display()
            print('_'*50)
            ask_()
        elif ask.lower()=='add':
            add()
        else:
            print('Wrong input!')
            

    else:
        print('Thank you')
    
if __name__=='__main__':
    ask_()