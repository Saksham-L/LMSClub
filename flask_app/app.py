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
	return """
<html>
<head>
	<style>
h1 {
  color: black;
  font-family: verdana;
  font-size: 300%;
}
p {
  color: red;
  font-family: courier;
  font-size: 160%;
}
table, th, td {
  border: 1px solid black;
}
</style>
</head>
<body>
<title>fst html</title>
<table style="width:100%" id="t01" >

<caption><h1>Calendar</h1></caption>
  <tr>
    <th>Day</th>
    <th>Time</th>
    <th>Subject</th>
  </tr>
  <tr>
    <td>Monday</td>
    <td>9:10-10:15</td>
    <td>P.E.</td>
    </tr>
 <tr>
    <td>Monday</td>
    <td>10:15-10:35</td>
    <td>Break</td>
    </tr>
    <tr>
    <td>Monday</td>
    <td>10:35-11:40</td>
    <td>Exploratory wheel</td>
    </tr>
    <tr>
    <td>Monday</td>
    <td>11:40-12:10</td>
    <td>Lunch</td>
    </tr>    
    <tr>
    <td>Monday</td>
    <td>12:10-1:15</td>
    <td>Science</td>
    </tr>    
    <tr>
    <td>Monday</td>
    <td>1:15-3:00</td>
    <td>Independent work time</td>
    </tr>  <tr>
    <td>Tuesday</td>
    <td>9:10-10:15</td>
    <td>Math</td>
    </tr>
 	<tr>
    <td>Tuesday</td>
    <td>10:15-10:35</td>
    <td>Break</td>
    </tr>
    <tr>
    <td>Tuesday</td>
    <td>10:35-11:40</td>
    <td>Language arts</td>
    </tr>
    <tr>
    <td>Tuesday</td>
    <td>11:40-12:10</td>
    <td>Lunch</td>
    </tr>    
    <tr>
    <td>Tuesday</td>
    <td>12:10-1:15</td>
    <td>Social Studies</td>
    </tr>    
    <tr>
    <td>Tuesday</td>
    <td>1:15-3:00</td>
    <td>Independent work time</td>
    </tr>

</table>
</body>
</html>
	"""
if __name__ == "__main__":
	app.dubug = True
	app.run(host="0.0.0.0", port=5000)