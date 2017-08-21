from flask import Flask, request, render_template
import json
app = Flask(__name__)

@app.route('/')
def home():
	return "<h1>this is home page</h1>"

@app.route('/users',methods=['GET','POST','PUT','DELETE'])
def users():
	if request.method=="GET":
		users=['user1','user2','user3']
		return json.dumps(users)
	elif request.method=="POST":
		msg=""
		try:
			data = request.json
			user=data.get('user')
			pwd=data.get('pasword')
			msg='login sucessfuly'
		except Exception as err:

			msg=err
		return json.dumps(msg)
@app.route('/user_reg', methods=['GET','POST'])
def user_reg():
	msg=""
	if request.method=="POST":
		data=request.form
		user=data.get('user')
		password=data.get("password")
		msg="success fully added."
		
	return render_template('home.html',msg=msg)

if __name__ == "__main__":
	app.run(debug=True)