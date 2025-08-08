from flask import Flask, render_template, request

# Create Flask app
app = Flask(__name__)

# Home route
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_name = request.form.get("name")
        return f"<h2>Hello, {user_name}!</h2>"
    return render_template("index.html")

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

