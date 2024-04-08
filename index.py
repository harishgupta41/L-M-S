from flask import Flask,redirect,url_for,render_template,request,make_response,session
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
app.secret_key='librarymanagementsystemsecretkey'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title='home')

@app.route('/login')
def signin():
    return render_template('login.html',title="login-pg")

@app.route('/register')
def register():
    return render_template('registration.html',title="registration-pg")

@app.route('/myProfile')
def myProfile():
    return render_template('userprofile.html',title="myProfile")

@app.route('/logging',methods=['POST'])
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

@app.route('/registration',methods=['POST'])
def registration():
    if request.method=='POST':
        data=[]
        data.append(request.form['username'])
        # print(username)
        data.append(request.form['fname'])
        data.append(request.form['phone'])
        data.append(request.form['email'])
        data.append(request.form['address'])
        admin=request.form.get('admin')
        admin="yes" if admin else "no"
        data.append(admin)
        data.append(request.form['passwd'])
        passwd=request.form['passwd']
        repasswd=request.form['repasswd']
        if passwd==repasswd:
            sOTP=methods.sendOTP(data[2])
            data.append(sOTP)
            session['userdata']=data
            return render_template("otpverify.html",title="otp-verification")
        else:
            return redirect('/')

@app.route('/verifyOtp', methods=['GET','POST'])
def verifyOtp():
    if request.method == 'POST':
        print(session['userdata'])
        rotp= request.form['rotp']
        if(rotp==session['userdata'][7]):
            cursor.execute('insert into users values("{0}","{1}","{2}","{3}","{4}","{5}","{6}")'.format(session['userdata'][0],session['userdata'][1],session['userdata'][2],session['userdata'][3],methods.sha256(session['userdata'][6]),session['userdata'][4],session['userdata'][5]))
            mydb.commit()
            session.clear()
            return redirect('/')
        return redirect('/register')
    
if __name__ == '__main__':
    app.run(port=5000,debug=True)