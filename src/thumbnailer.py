import os
import subprocess

class Thumbnailer:

    @staticmethod
    def get_thumbnail(movie, size=1280):
        file_name = os.path.splitext(movie.full_path())[0]
        thumbnail_path = "{0}.png".format(file_name)

        try:
            if not os.path.exists(thumbnail_path):
                subprocess.call(["ffmpegthumbnailer",
                                 "-i",
                                 movie.full_path(),
                                 "-o",
                                 thumbnail_path,
                                 "-s",
                                 str(size)
                               ])
            return thumbnail_path
        except:
            return None


