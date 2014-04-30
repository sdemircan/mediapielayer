import os
import subprocess
import logging

logger = logging.getLogger(__name__)

class Thumbnailer:

    @staticmethod
    def get_thumbnail(movie, size=1280):
        file_name = os.path.splitext(movie.full_path())[0]
        thumbnail_path = "{0}.png".format(file_name)

        try:
            if not os.path.exists(thumbnail_path):
                subprocess.check_call(["ffmpegthumbnailer",
                                 "-i",
                                 movie.full_path(),
                                 "-o",
                                 thumbnail_path,
                                 "-s",
                                 str(size)
                               ])
            return thumbnail_path
        except OSError as e:
            logger.exception("Error while creating thumbnail for %s.%s\n%s",
                              "Please check ffmpegthumbnailer installed properly",
                              file_name, e
                             )
        except subprocess.CalledProcessError as e:
            logger.exception("Error occured while creating \
                               thumbnail with ffmpegthumbnailer for %s\n%s",e
                             )

