from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Yeh error throw karega agar input nahi mila
        name = request.form['username']

        # Yeh safe hai, agar input nahi mila toh None return karega
        email = request.form.get('email')

        return f"Hello {name}, your email is {email}"

    return '''
        <form method="POST">
            Name: <input type="text" name="username"><br>
            Email: <input type="text" name="email"><br>
            <input type="submit">
        </form>
    '''
