from flask import Flask, request

app = Flask(__name__)

users = {
    "admin": "StrongPass@123"
}

@app.route('/')
def home():

    return '''

    <h2>Secure Login</h2>

    <form method="POST" action="/login">

        Username:
        <input type="text" name="username"><br><br>

        Password:
        <input type="password" name="password"><br><br>

        <input type="submit" value="Login">

    </form>

    '''

@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    password = request.form['password']

    if len(username) > 20:

        return "Invalid Username"

    if username in users and users[username] == password:

        return "Login Successful"

    return "Invalid Credentials"

if __name__ == '__main__':

    app.run(debug=False)