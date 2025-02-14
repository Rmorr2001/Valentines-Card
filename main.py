from flask import Flask, render_template, request, redirect
from waitress import serve

app = Flask(__name__)

# Home routes
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        password = password.lower()
        # Add your authentication logic here
        if password == "lovebug":
            return redirect('/valentine')  # Changed to string path
        else:
            return 'Invalid credentials', 401
    return render_template('login.html')

@app.route('/valentine')  # Changed route decorator
def valentine():
    return render_template('valentines-card.html')  # Added return statement

if __name__ == "__main__":
    # Waitress is a production-grade WSGI server, unlike Flask's built-in server
    # It's more secure and can handle multiple concurrent connections
    serve(app, host="0.0.0.0", port=8000)