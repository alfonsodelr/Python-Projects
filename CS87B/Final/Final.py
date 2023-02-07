import sqlite3

def main():
    conn = sqlite3.connect('mylist.db')
    c = conn.cursor()
    c.execute(""" CREATE TABLE IF NOT EXISTS datapoints (
                ID text, 
                Height integer
    )""") #I assume ID here is alphanumeric since we can easily convert it to int

    c.execute("INSERT INTO datapoints VALUES (?,?)", ("data_point_1", 8)) #inserted test values
    c.execute("INSERT INTO datapoints VALUES (?,?)", ("data_point_2", 10)) #inserted test values
    conn.commit()

    c.execute("SELECT AVG(Height) FROM datapoints") #takes average of height of all existing data in db

    avg = c.fetchone()[0] # assigns average to avg var
    print('average of db: ', avg) #prints avg

    c.execute("UPDATE datapoints SET Height = 0 WHERE Height<?", (avg,)) #changes all Heights that are < 10 to 0
    c.execute("SELECT * FROM datapoints WHERE Height=0") 

    print(c.fetchall()) #prints the values of the data points that have height = 0 

    print('total changes: ', conn.total_changes)

    conn.close()

main()