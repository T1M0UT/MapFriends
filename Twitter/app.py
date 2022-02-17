import friends_locator

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        user = request.form["name"]
        try:
            if friends_locator.search(user):
                return redirect(url_for("friends_map"))
            else:
                return render_template("index.html", error='Wrong username')
        except Exception as e:
            if str(e) == 'HTTP Error 429: Too Many Requests':
                return render_template("index.html", error='Too Many Requests')
            return render_template("index.html", error=str(e))
    return render_template("index.html")


@app.route("/map")
def friends_map():
    return render_template("MapFriends.html")


if __name__ == "__main__":
    app.run(debug=True)
