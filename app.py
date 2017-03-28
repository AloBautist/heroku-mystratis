#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

import bottle
from bottle import route,run

bottle.debug(True)

@route('/')
def index():
	return "<h1>Hola Mundo 2!!!</h1>"

run(host='0.0.0.0',port=argv[1])
