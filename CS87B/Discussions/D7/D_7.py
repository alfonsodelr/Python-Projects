import sqlite3
from D7_class import Player

def insert(c, player):
    c.execute("INSERT INTO Players VALUES (?, ?, ?)", (player.userName, player.gamerTag, player.playerID))


def traverse(c, userName):
    c.execute("SELECT * FROM Players WHERE userName=?", (userName,))

    print(c.fetchall())

def Create(c):
    c.execute("""CREATE TABLE IF NOT EXISTS Players (
                userName text,
                gamerTag text,
                ID integer
                )""")

def main():

    conn = sqlite3.connect('employee.db')

    c = conn.cursor()

    Create(c)

    user_1 = Player('user_1', 'gamertag_1', 10231)
    user_2 = Player('user_2', 'gamertag_2', 12312)

    insert(c, user_1)
    insert(c, user_2)
    conn.commit()

    traverse(c, 'user_1')
    traverse(c, 'user_2')

    conn.close()

main()


#c.execute("INSERT INTO employees VALUES ('Mary', 'Schafer', 70000)")

#c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))

#c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})

#conn.commit()


#c.execute("SELECT * FROM employees WHERE last='Schafer'")

#c.execute("SELECT * FROM employees WHERE last=?", ('Schafer',))

#print(c.fetchall())

#c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Doe'})

#print(c.fetchall())

#conn.commit()

#conn.close()