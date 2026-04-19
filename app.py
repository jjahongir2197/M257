from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email == "admin@gmail.com" and password == "123456":
            message = "Login successful ✅"
        else:
            message = "Xato login ❌"

    return render_template("login.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
