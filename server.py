from flask import Flask, render_template, request, redirect

from user import User
app = Flask(__name__)
@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("read.html", all_users=users)

@app.route("/create_user")
def create_user():
    return render_template("create.html")

from user import User
@app.route('/created', methods=["POST"])
def created():

    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    User.save(data)
    return redirect('/')

            
if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)


