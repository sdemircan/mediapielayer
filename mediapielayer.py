from flask import Flask, request, render_template, send_from_directory
from src.movie import MovieLister

app = Flask(__name__)
app.config.from_pyfile("settings.conf")

@app.route("/")
def list_movies():
    lister = MovieLister(app.config['TORRENTROOT'], app.config['EXTENSIONS'])
    return render_template("movies.html", movies=lister.list())

@app.route('/img/<path:filename>')
def send_file(filename):
      return send_from_directory('/', filename)

@app.route("/<movie>")
def watch_movie(movie):
    pass

@app.route("/<movie>/subtitle")
def find_subtitle(movie):
    pass

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
