from flask import Flask, render_template, request, redirect, url_for

app = Flask(_name_)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the contact form submission
@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Here you can add logic to save the message or send an email
        print(f"Name: {name}, Email: {email}, Message: {message}")
        return redirect(url_for('index'))

if _name_ == '_main_':
    app.run(debug=True)
