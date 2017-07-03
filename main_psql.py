import sys
import db_qur 

def crud_postgresql(con):
    print "-----------------------"
    print "1.Create"
    print "2.Retrive"
    print "3.Insert"
    print "4.Delete"
    print "5.Update"
    print "6.Exit"
    print "-----------------------"
    user = raw_input("Enter your choice?")

    if user == "1":
        db_qur.create_table_post(con)
        crud_postgresql(con)
    elif user == "2":
        db_qur.retrive_data_post(con)
        crud_postgresql(con)
    elif user == "3":
        db_qur.insert_data_post(con)
        crud_postgresql(con)
    elif user == "4":
        db_qur.delete_data_post(con)
        crud_postgresql(con)
    elif user == "5":
        db_qur.update_data_post(con)
        crud_postgresql(con)
    elif user == "6":
        exit()

def choice():
    con = db_qur.connection_postgresql()
    crud_postgresql(con)

choice()