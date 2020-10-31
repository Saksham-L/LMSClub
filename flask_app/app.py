from flask import Flask

app=Flask(__name__)
@app.route('/')
def index():
	return '<h1 align=center> Please enter / and then your name in the address bar<h1>'
@app.route('/<name>')
def name(name):
	return '<h1> Hello {}</h1><h2> Please go to the calendar page to see your <a href="http://127.0.0.1:5000/calendar">calendar</a><h2>'.format(name)
@app.route('/calendar')
def calendar():
	return '<h1 style="color:red;">Day       Time             Subject <br>-------------------------------------- <br>Monday   9:10-10:15			P.E.<br>Monday   10:15-10:35			Break <br>Monday   10:35-11:40			Exploratory wheel<br>Monday   11:40-12:10			Lunch<br>Monday   12:10-1:15			Science<br>Monday   1:15-3:00			Independent work time<br>Tuesday  9:10-10:15			Math<br>Tuesday  10:35-11:40			Language arts<br>Tuesday  11:40-12:10			Lunch<br>Tuesday  12:10-1:15			Social Studies<br>Tuesday  1:15-3:00          Independent work</h1>'
if __name__ == "__main__":
	app.dubug = True
	app.run(host="0.0.0.0", port=5000)