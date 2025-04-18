from flask import Flask, request, redirect, url_for, send_from_directory, flash, get_flashed_messages, render_template_string

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

@app.route('/', methods=['GET'])
def index():
    return send_from_directory('.', 'index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username', '').strip()
    email = request.form.get('email', '').strip()
    password = request.form.get('password', '')

    errors = []

    if not username:
        errors.append('Username required')
    if '@' not in email:
        errors.append('Invalid email')
    if len(password) < 6:
        errors.append('Password too short')

    if errors:
        # Show errors as a simple HTML page
        error_html = '<br>'.join(errors)
        return f"<h3>Registration Failed</h3><p>{error_html}</p><a href='/'>Go back</a>"
    else:
        return "<h3>Registration Successful!</h3><a href='/'>Go back</a>"

if __name__ == '__main__':
    app.run(debug=True)