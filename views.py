from bottle import template



def main_page():
	return template(open( 'templates/main.html').read())

