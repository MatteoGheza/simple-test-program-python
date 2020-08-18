try:
    from version import __version__
except ImportError:
    import sys
    import os.path
    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(os.path.dirname(path))) #from https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/__main__.py
    try:
        from version import __version__
    except ImportError:
        from .version import __version__

__productname__ = 'simpletestprogram'
__author__      = "Matteo Gheza"
__author_email__= "matteo@matteogheza.it"
__description__ = "A simple multi-platform test program in Python"
__license__  = "Licensed under the GNU GPL v3 or any later version"
__bigcopyright__ = """%(__productname__)s %(__version__)s
  %(__license__)s""" % locals()
__homepage__ = "https://github.com/MatteoGheza/simple-test-program-python"

banner = __bigcopyright__

__all__ = ['version', 'init']

if __name__ == '__main__':
    from init import main
    main()