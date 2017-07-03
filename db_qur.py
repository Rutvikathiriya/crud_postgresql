from db_con import *
import psycopg2

def create_table_post(con):
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Emp")
        cur.execute(
            "CREATE TABLE Emp(Id SERIAL PRIMARY KEY, Name VARCHAR(25), Company_Name VARCHAR(25), Designation VARCHAR(25));")
        print 'Employee Table created'

def insert_data_post(con):
    with con:
        try:
            cur = con.cursor()
            Name = raw_input("Enter Your Name : ")
            Company_Name = raw_input("Enter Your Company Name : ")
            Designation = raw_input("Enter Your Designation : ")
            cur.execute("INSERT INTO Emp  (Name, Company_Name, Designation) VALUES(%s, %s, %s )",
                        (Name, Company_Name, Designation))
            print "Record Inserted"
            con.commit()
        except Exception as e:
            print e

def retrive_data_post(con):
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Emp")

        rows = cur.fetchall()
        for row in rows:
            if rows == None:
                print 'Table is Empty'
                break
            else:
                print('ID: {0} Name: {1} Company Name: {2} Designation: {3}'.format(
                    row[0], row[1], row[2], row[3]))

def update_data_post(con):
    with con:
        try:
            cur = con.cursor()
            cur.execute("SELECT * FROM Emp")
            rows = cur.fetchall()
            for row in rows:
                print('ID: {0} Name: {1} Company Name: {2} Designation: {3}'.format(
                    row[0], row[1], row[2], row[3]))

            e_id = input("Enter id You want to update :")
            name = raw_input("Enter Name for Update Record : ")
            cname = raw_input("Enter Company Name for Update Record : ")
            deg = raw_input("Enter Designation for Update Record : ")

            cur.execute("UPDATE Emp SET name =%s, Company_Name = %s, Designation = %s WHERE Id = %s",
                        (name, cname, deg, e_id))

            print "Number of rows updated:",  cur.rowcount
            if cur.rowcount == 0:
                print 'Record Not Updated'
        except TypeError as e:
            print 'ID Not Exist'

def delete_data_post(con):
    with con:
        try:
            cur = con.cursor()
            #cur = con.cursor(cursor_factory=pdb.extras.DictCursor)
            cur.execute("SELECT * FROM Emp")
            rows = cur.fetchall()
            for row in rows:
                print('ID: {0} Name: {1} Company Name: {2} Designation: {3} '.format(
                    row[0], row[1], row[2], row[3]))

            id = raw_input("Enter ID for Delete Record : ")
            cur.execute("DELETE FROM Emp WHERE Id = %s", id)
            print "Number of rows deleted:", cur.rowcount

        except TypeError as e:
            print 'ID Not Exist'