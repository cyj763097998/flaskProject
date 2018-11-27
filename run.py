#encoding: utf-8 
from flask import Flask,render_template
from conf import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
@app.route('/index/')
def index():
	return render_template('index.html')

@app.route('/rule/')
def rule():
	return render_template('rule.html')
@app.route('/admin/')
def admin():
	return render_template('admin.html')
@app.route('/role/')
def role():
	return render_template('role.html')


if __name__ == '__main__':
	app.run(port=50001)