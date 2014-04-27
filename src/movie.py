import os
import fnmatch

class Movie:
    def __init__(self, path, name):
        self.path = path
        self.name = name

    def path(self):
        return os.path.join(self.path, self.name)

    def pretty_name(self):
        file_name = os.path.splitext(self.name)[0]
        return file_name.replace('.', ' ').title()

class MovieLister:
    def __init__(self, basedir, extensions):
        self.basedir = basedir
        self.extensions = extensions

    def list(self):
        for root, dirs, files in os.walk(self.basedir):
            for extension in self.extensions:
                for filename in fnmatch.filter(files, extension):
                    yield Movie(root.decode("utf8"), filename.decode("utf8"))
