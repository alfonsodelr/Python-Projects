import sqlite3

def func(conn, mylist):
    verified = 0
    total = 0
    c = conn.cursor()

    for i in range (0, len(mylist)):
        
        c.execute("""CREATE TABLE IF NOT EXISTS mytable (
                    a integer,
                    b real,
                    c text,
                    verified integer
                    )""")

        if mylist[i][1] < 0.0:
            mylist[i][1] = 0.0
            verified = 0
        else:
            verified = 1

        c.execute("INSERT INTO mytable VALUES (?,?,?,?)", (mylist[i][0], mylist[i][1], mylist[i][2], verified))
        
        conn.commit()
        variableeeeee = conn.total_changes

        c.execute("SELECT * FROM mytable WHERE b>=0.0")
        total += c.fetchall()[i][1]

    return variableeeeee
        

def main():

    conn = sqlite3.connect('mylistdb.sqlite')

    mylist = [(1, 2.2, 'hello'), (2, 1.1, 'nice'), (5, 2.3, 'hello')]

    total = func(conn, mylist)

    print(total)

    conn.close()

    

main()