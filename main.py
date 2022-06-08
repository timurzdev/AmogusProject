# Python version - 3.8.5
# Flask version - 2.1.2

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('home.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            username = request.form['username']
            with sqlite3.connect("database.db") as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO users (username) VALUES (?)", [username])
                conn.commit()
        except:
            conn.rollback()
        finally:
            return render_template("home.html")
            conn.close()


@app.route('/list')
def list():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute("SELECT * FROM users")

    rows = cur.fetchall()
    return render_template("list.html", rows=rows)


if __name__ == '__main__':
    conn = sqlite3.connect('database.db')

    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
               userid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               username TEXT);
    """)
    conn.commit()
    # username = 'test'
    # cur.execute("INSERT INTO users (username) VALUES (?)", [username])
    # conn.commit()
    # cur.execute("SELECT * FROM users")
    # print(cur.fetchall())
    # conn.commit()
