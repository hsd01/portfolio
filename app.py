"""from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
"""
from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)

# Email Config (Use Gmail App Password)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ashuhemantsingh@gmail.com'
app.config['MAIL_PASSWORD'] = 'istgnisjoihbeazb'

mail = Mail(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    msg = Message(
        subject=f"Portfolio Contact from {name}",
        sender=email,
        recipients=['hemant@dhanwars.in'],
        body=message
    )
    mail.send(msg)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
