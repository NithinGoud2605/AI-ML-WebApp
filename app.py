import pyodbc
from flask import Flask, request, render_template

app = Flask(__name__)

# Database connection string
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=retail-sql-server-cc.database.windows.net;'
    'DATABASE=Userdatabase;'
    'UID=NithinGoud;'
    'PWD=password@123'
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    # Insert user into database
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO users (username, password, email)
        VALUES (?, ?, ?)
    """, (username, password, email))
    conn.commit()

    return f"User {username} registered successfully!"

if __name__ == '__main__':
    app.run(debug=True)
