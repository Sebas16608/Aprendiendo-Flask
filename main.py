from flask import Flask, request, make_response, redirect

app = Flask(__name__)


@app.route("/index")
def index():
    user_ip_unformation = request.remote_addr
    response = make_response(  redirect("/show-information-address"))
    response.set_cookie("user_ip_unformation", user_ip_unformation)
    return response

@app.route("/show-information-address")
def show_information():
    user_ip = request.cookies.get("user_ip_unformation")
    return f"Hola que tal, tu direccion ip es {user_ip}"
app.run(host="0.0.0.0", port=3000, debug=True)