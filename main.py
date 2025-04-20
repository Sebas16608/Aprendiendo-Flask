from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

items = ["Item 1", "Item 2", "Item 3", "Item 4"]
@app.route("/index")
def index():
    user_ip_unformation = request.remote_addr
    response = make_response(  redirect("/show-information-address"))
    response.set_cookie("user_ip_unformation", user_ip_unformation)
    return response

@app.route("/show-information-address")
def show_information():
    user_ip = request.cookies.get("user_ip_unformation")
    context = {

        "user_ip": user_ip,
        "items": items
    }
    return render_template("ip_information.html", **context)



app.run(host="0.0.0.0", port=3000, debug=True)