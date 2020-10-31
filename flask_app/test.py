from flask import Flask

test=Flask(__name__)

@test.route('/<name>')
def index(name):
	return '<h1> hello  {}</h1> <table> <th> <tr> hello again </tr> </th>'.format(name)

if __name__ == "__main__":
	test.dubug = True
	test.run(host="0.0.0.0", port=8000)