import os
import subprocess
import logging

logger = logging.getLogger(__name__)

class Thumbnailer:

    def __init__(self, basedir):
        self.basedir = basedir

    def get_thumbnail(self, movie, size=1280):
        full_path = os.path.join(self.basedir, movie.path, movie.name)
        file_name = os.path.splitext(full_path)[0]
        thumbnail_path = "{0}.png".format(file_name)

        try:
            if not os.path.exists(thumbnail_path):
                subprocess.check_call(["ffmpegthumbnailer",
                                 "-i",
                                 full_path,
                                 "-o",
                                 thumbnail_path,
                                 "-s",
                                 str(size)
                               ])
            return os.path.relpath(thumbnail_path, self.basedir)
        except OSError as e:
            logger.exception("Error while creating thumbnail for %s.%s\n%s",
                              "Please check ffmpegthumbnailer installed properly",
                              file_name, e
                             )
        except subprocess.CalledProcessError as e:
            logger.exception("Error occured while creating \
                               thumbnail with ffmpegthumbnailer for %s\n%s",e
                             )
