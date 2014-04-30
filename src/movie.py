import os
import fnmatch
import mimetypes
from src.thumbnailer import Thumbnailer

class Movie:
    def __init__(self, path, name, thumbnailer):
        self.path = path
        self.name = name
        self.thumbnailer = thumbnailer

    def full_path(self):
        return os.path.join(self.path, self.name)

    def pretty_name(self):
        file_name = os.path.splitext(self.name)[0]
        return file_name.replace('.', ' ').title()

    def video(self):
        return self.full_path()

    def thumbnail(self):
        return self.thumbnailer.get_thumbnail(self)

    def mime(self):
        return mimetypes.guess_type(self.full_path())[0]

class MovieLister:
    def __init__(self, basedir, extensions):
        self.basedir = basedir
        self.extensions = extensions
        self.thumbnailer = Thumbnailer(basedir)

    def list(self):
        for root, dirs, files in os.walk(self.basedir):
            for extension in self.extensions:
                for filename in fnmatch.filter(files, extension):
                    relative_path = os.path.relpath(root.decode("utf8"), self.basedir)
                    yield Movie(relative_path, filename.decode("utf8"), self.thumbnailer)

    def get(self, movie):
        full_path = os.path.join(self.basedir, movie)
        if not os.path.isfile(full_path):
            return None

        for extension in self.extensions:
            if not fnmatch.filter([full_path], extension):
                path, name = os.path.split(movie)
                return Movie(path, name, self.thumbnailer)

        return None # No filter matched, invalid movie name
