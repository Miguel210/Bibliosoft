from flask import Flask, flash, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'mysecretkey'

app.secret_key = 'mysecretkey'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'bibliosoft'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/perfil')
def inicio():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM perfil')
    data = cur.fetchall()
    cur.close()
    return render_template('perfil.html', perfiles=data)

if __name__ == '__main__':
    app.run(debug=True)