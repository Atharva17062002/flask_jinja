from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)


user_data = [
    {
        "username": "John",
        "password": "1234",
        "data": [
            {"salary": 1000, "expenses": 500, "savings": 500},
        ],
    },
    {
        "username": "Jane",
        "password": "5678",
        "data": [
            {"salary": 2000, "expenses": 1000, "savings": 1000},
        ],
    },
]


@app.route("/index/<username>")
def hello_world(username):

    for user in user_data:
        if user["username"] == username:
            return render_template(
                "index.html", user=user["username"], data=user["data"]
            )

    return "User not found", 404


@app.route("/login", methods=["GET", "POST"])
def login():
    data = request.form

    if request.method == "POST":
        for user in user_data:
            if user["username"] == data.get("username") and user[
                "password"
            ] == data.get("password"):
                return redirect(f"/index/{user['username']}")
        return (
            render_template("login.html", error="Invalid username or password"),
            401,
        )
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    data = request.form

    if request.method == "POST":
        for user in user_data:
            if user["username"] == data.get("username"):
                return (
                    render_template("register.html", error="Username already exists"),
                    401,
                )
        user_data.append(
            {
                "username": data.get("username"),
                "password": data.get("password"),
                "data": [],
            }
        )
        return redirect("/login")
    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)