from flask import Flask, request, abort, render_template, send_from_directory
from src.movie import MovieLister
import logging

app = Flask(__name__)
app.config.from_pyfile("settings.conf")

#logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def list_movies():
    lister = MovieLister(app.config['TORRENTROOT'], app.config['EXTENSIONS'])
    return render_template("movies.html", movies=lister.list())

@app.route('/dynamic/<path:filename>')
def send_file(filename):
      return send_from_directory(app.config['TORRENTROOT'], filename)

@app.route("/movie/<path:movie>")
def watch_movie(movie):
    lister = MovieLister(app.config['TORRENTROOT'], app.config['EXTENSIONS'])
    m = lister.get(movie)
    if m:
        return render_template('player.html', movie=m)
    else:
        return abort(404)

@app.route("/<movie>/subtitle")
def find_subtitle(movie):
    pass

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
