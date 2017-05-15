from bottle import template

def main_page():
	file = open( 'templates/main.html').read()
	values ={
		'area': '1',
		'type': 'other',
		'points': [[1,2],[3,4]],

	}
	return template(file, **values)

