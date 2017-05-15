#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
import bottle
from bottle import route,run
from views import *

bottle.debug(True)

@route('/')
def index():
	return main_page()



if __name__ == '__main__':
	run(host='0.0.0.0',port=argv[1])
