from flask import Flask, request, render_template

app = Flask(__name__)
app.config.from_pyfile("settings.conf")

@app.route("/")
def list_movies():
    pass

@app.route("/<movie>")
def watch_movie(movie):
    pass

@app.route("/<movie>/subtitle")
def find_subtitle(movie):
    pass

if __name__ == '__main__':
    app.run(debug=True)
