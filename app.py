from flask import Flask, render_template

app = Flask(__name__)

# The following routes are needed
#   GET /about
#   GET /movies
#   GET /songs
#   GET /books
#   GET /courses
#   GET /contact


@app.route("/", methods=["GET"])
def home():
    """Home page — already built as the example for students to follow."""
    return render_template("home.html")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )