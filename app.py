from flask import Flask, flash, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'mysecretkey'

app.secret_key = 'mysecretkey'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pass'
app.config['MYSQL_DB'] = 'biblioteca'
mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM perfil")
    data = cur.fetchall()
    cur.close()
    print(data)
    return render_template('index.html', perfiles=data)


if __name__ == '__main__':
    app.run(debug=True)