import psycopg2

def connection_postgresql():
    try:
        con = psycopg2.connect(user="rutvi", password = "rutvi", database="mytestdb", host="localhost", port ="5432")
        cur = con.cursor()
        cur.execute('SELECT version()')
        ver = cur.fetchone()
        print ver
        return con

    except psycopg2.DatabaseError, e:
        print 'Error %s' % e    
        sys.exit(1)
