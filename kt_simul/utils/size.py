from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

import os

def get_folder_size(folder):
    """
    Determine size of a given folder in MBytes
    """
    folder_size = 0
    for (path, dirs, files) in os.walk(folder):
      for file in files:
        filename = os.path.join(path, file)
        folder_size += os.path.getsize(filename)
    return round(folder_size/(1024*1024.0), 1)
