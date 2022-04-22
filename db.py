from turtle import textinput
import psycopg2

#establishing the connection
conn = psycopg2.connect(database="Information", user='postgres', 
password='postgres', host='10.226.253.225', port= 5432)

#Creating a cur object using the cur() method
cur =conn.cursor()

#Executing an SQL function using the execute() method
cur.execute("select version()")

# Fetch a single row using fetchone() method.
data =cur.fetchone()
print("Connection established to: ", data)

def insert(id, fname, lname, email, phone):
    #grab data and insert
    query = """INSERT INTO Employees(empID, Fname, Lname, email, phone) 
                  values (%s, %s, %s, %s, %s)"""
    record = (id, fname, lname, email, phone)
    cur.execute(query, record)
    conn.commit()
   
def delete(id):
    #remove employee
   cur.execute("""DELETE FROM Employees WHERE empID=%s""", (id,))
   conn.commit()

def update(id, credit):
    cur.execute("UPDATE Employees SET credit=%s WHERE empID=%s", (credit, id))
    conn.commit()

#search database for employee or admin ID
def search(id):
   cur.execute("SELECT empID FROM Employees where empID = %s", (id,))
   Ename = cur.fetchall
   cur.execute("SELECT adminID FROM Administrator where adminID =%s", (id,))
   Aname = cur.fetchall
   return Ename, Aname #returns everything, but must use 'for name in search:'

def get_credit(id):
   cur.execute("SELECT credit FROM Employee WHERE empID=%s", (id,))

def trig_credit(id, num):
   cur.execute("UPDATE Employees Set credit=%s WHERE empID=%s", (num, id))
   conn.commit()

def close():
   conn.close()
