#!/usr/bin/env python
from __future__ import unicode_literals
import sys

import os.path
path = os.path.realpath(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(path))) #from https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/__main__.py

from simpletestprogram import init

if __name__ == '__main__':
    init.main()