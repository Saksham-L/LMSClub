from flask import Flask

app=Flask(__name__)
@app.route('/')
def index():
	return """<body bgcolor=black><h1 style="text-align:center;color: crimson;" > Please enter / and then your name in the address bar</h1></body>"""
@app.route('/<name>')
def name(name):
	return '<body bgcolor=black><h1 style="text-align:center;color: crimson;"> Hello {}</h1></boday><h2 style="color: crimson;"> Please go to the calendar page to see your <a href="http://127.0.0.1:5000/calendar">calendar</a><h2>'.format(name)
@app.route('/calendar')
def calendar():
	return """
<html>
<head>
	<style>
h1 {
  color: crimson;
  font-family: verdana;
  font-size: 300%;

}
p {
  background color: crimson;
  color: red;
  font-family: courier;
  font-size: 160%;
}
table, th, td {
  border: 0.5px solid red; border-collapse: collapse;
  font-weight: bold;
}
#t01 {
  width: 100%;
  color: crimson;
   background-color: black;

}

</style>
</head>
<body bgcolor=black>
<title>fst html</title>
<table id="t01">

<caption><h1 style=background color: black;>Calendar</h1></caption>
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