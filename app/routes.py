from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Pawel'}
	posts = [
		{
			'author': {'username': 'John'},
			'body': 'foo'
		},
		{
			'author': {'username': 'Susan'},
			'body': 'bar'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts) 
