from os.path import join
import sys


def resource_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return join(sys._MEIPASS, filename)
    else:
        return filename
