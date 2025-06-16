from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import unittest

app = Flask(__name__)

bootstrap = Bootstrap(app)

app.config["SECRET_KEY"] = "S3b@sr1234"

items = ["Arroz", "Huevos", "Café", "Leche"]


class LoginForm(FlaskForm):
    username = StringField("Nombre del Usuario", validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    submit = SubmitField("Enviar datos")

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found_endpoint(error):
    return render_template('404.html', error=error)


@app.route("/index")
def index():
    user_ip_information = request.remote_addr
    response = make_response(  redirect("/show-information-address"))
    session["user_ip_information"] = user_ip_information

    return response

@app.route("/show-information-address", methods = ["GET", "POST"])
def show_information():
    user_ip = session.get("user_ip_information")
    username = session.get("username")
    login_form = LoginForm()
    context = {
        "user_ip": user_ip,
        "items": items,
        "login_form": login_form,
        "username": username
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        session["username"] = username
        flash("Nombre de usuario registrado correctamente")
        return redirect(url_for("index"))
    return render_template("ip_information.html", **context)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)