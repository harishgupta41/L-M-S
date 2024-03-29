from flask import Flask,redirect,url_for,render_template,request,make_response
import mysql.connector
import uuid
import methods

# created sql connection
mydb=mysql.connector.connect(
    host="localhost",database="library",user="harry",password="dl3san3581"
)
cursor=mydb.cursor()

# flask app
app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title='home')

@app.route('/signin')
def signin():
    return render_template('login.html',title="signin-pg")

@app.route('/login',methods=['POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['passwd']
        cursor.execute("select * from users where username='{0}' and passwd='{1}'".format(username,methods.sha256(password)))
        data = cursor.fetchall()
        if(data):
            resp=make_response(redirect('/'))
            resp.set_cookie('user',username)
            return resp       

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(port=5000,debug=True)