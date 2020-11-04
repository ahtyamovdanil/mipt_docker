import mysql.connector
from tabulate import tabulate
import csv

config = {'user': 'root',
          'password': '24812481',
          'host': 'db'
}

try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

except mysql.connector.Error as err:
    print("Failed: {}".format(err))
    with open('logs/log', 'w') as f:
        f.writelines("Failed: {}".format(err))
    exit(1)

# config with the new database
config = {'user': 'root',
          'password': '24812481',
          'host': 'db',
          'database': 'mydatabase'
}

try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    # create table
    cursor.execute("DROP TABLE IF EXISTS mytable")
    cursor.execute("CREATE TABLE IF NOT EXISTS mytable (column1 varchar(255), column2 int)")

    # read csv and insert data from it to the created table
    with open('data/data.csv', 'r') as csv_file:
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            cursor.execute("""INSERT INTO mytable(column1, column2) VALUES("%s", "%s")""", [row[0], int(row[1])])

    # get inserted data
    cursor.execute("SELECT * from mytable")
    records = cursor.fetchall()

    # print inserted data to console
    field_names = [i[0] for i in cursor.description]
    print(tabulate(records, headers=field_names))

    # print inserted data to the log file 
    with open('logs/log', 'w') as f:
        f.writelines(tabulate(records, headers=field_names))
        #close the connection to the database.
        cnx.commit()
        cursor.close()

except mysql.connector.Error as err:
    print("Failed: {}".format(err))
    with open('logs/log', 'w') as f:
        f.writelines("Failed: {}".format(err))
    exit(1)
