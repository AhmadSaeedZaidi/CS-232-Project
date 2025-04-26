#imports
from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from routes.menu_routes import menu_bp

app = Flask(__name__)
app.register_blueprint(menu_bp)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
    