from flask import Flask
import mysql.connector
from tabulate import tabulate

app = Flask(__name__)

@app.route('/')
def get_table():
    config = {'user': 'root',
          'password': '24812481',
          'host': 'db',
          'database': 'mydatabase'
    }
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute("SELECT * from mytable")
    records = cursor.fetchall()
    field_names = [i[0] for i in cursor.description]
    return tabulate(records, headers=field_names, tablefmt='html')


@app.route('/health')
def is_health():
    return '200'  


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return '404'


if __name__ == '__main__':
    app.run(host='0.0.0.0')