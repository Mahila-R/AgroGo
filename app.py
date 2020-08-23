import os
from werkzeug import secure_filename
import matplotlib.pyplot as plt
from flask import Flask,render_template,redirect,request,url_for
from flaskext.mysql import MySQL
app=Flask(__name__)
mysql=MySQL()


app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='agro'
app.config['MYSQL_DATABASE_HOST']='localhost'
mysql.init_app(app)

@app.route("/index",methods=['GET','POST'])
def index():
    conn=mysql.connect()
    cur=conn.cursor()
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        id=request.args.get('data')
        cur.execute("SELECT * FROM `register` WHERE `username`='"+username+"' AND `password`='"+password+"'")
        data=cur.fetchone()
        if data[2]==username and data[3]==password:
            if data[6]=="farmer":
                return redirect(url_for('home',data=data[0]))
            elif data[6]=="investor":
                return redirect(url_for('investor',data=data[0]))
        else:
            error= "invalid credentials"
            return render_template("login.html",error=error)
    else:
        return render_template("index.html")

@app.route("/register",methods=['GET','POST'])
def register():
    if request.method=='POST':
        name=request.form['name']
        username=request.form['username']
        password=request.form['password']
        address=request.form['address']
        phone=request.form['phone']
        usertype=request.form['usertype']
        conn=mysql.connect()
        cur=conn.cursor()
        cur.execute("INSERT INTO `register`(`name`, `username`, `password`, `phone`, `adddress`, `usertype`) VALUES (%s,%s,%s,%s,%s,%s)",(name,username,password,phone,address,usertype))
        conn.commit()
        return redirect('index')
    else:
        return render_template("register.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/addcrops",methods=['GET','POST'])
def addcrops():
    if request.method=='POST':
        farmerid=request.form['farmerid']
        cropid=request.form['cropid']
        cropname=request.form['cropname']
        duration=request.form['duration']
        soiltype=request.form['soiltype']
        desp=request.form['desp']
        APP_PATH_ROUTE=os.path.dirname(os.path.abspath(__file__))
        target=os.path.join(APP_PATH_ROUTE,'uploads')
        UPLOAD_FOLDER='{}/static/uploads/'.format(APP_PATH_ROUTE)
        app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
        files=request.files['files']
        f=os.path.join(UPLOAD_FOLDER,files.filename)
        files.save(f)
        filename=secure_filename(files.filename)
        conn=mysql.connect()
        cur=conn.cursor()
        cur.execute("INSERT INTO `addcrop`(`farmerid`, `cropid`, `cropname`, `duration`, `soiltype`,`desp`,`image`)VALUES (%s,%s,%s,%s,%s,%s,%s)",(farmerid,cropid,cropname,duration,soiltype,desp,filename))
        conn.commit()
        return redirect('viewcrops')
    else:
        return render_template("addcrops.html")


@app.route("/viewcrops")
def viewcrops():
    conn=mysql.connect()
    cur=conn.cursor()
    cur.execute("SELECT * FROM `addcrop`")
    data=cur.fetchall()
    return render_template("viewcrops.html",crop=data)

@app.route("/editcr",methods=['GET','POST'])
def editcr():
    conn=mysql.connect()
    cursor=conn.cursor()
    addcrop=request.args.get('id')
    cursor.execute("SELECT * FROM `addcrop` WHERE `id`='"+addcrop+"'")
    crop=cursor.fetchone()
    if request.method=='POST':
        farmerid=request.form['farmerid']
        cropid=request.form['cropid']
        cropname=request.form['cropname']
        duration=request.form['duration']
        soiltype=request.form['soiltype']
        desp=request.form['desp']
        conn=mysql.connect()
        cur=conn.cursor()
        sql="UPDATE `addcrop` SET `farmerid`='"+farmerid+"',`cropid`='"+cropid+"',`cropname`='"+cropname+"',`duration`='"+duration+"',`soiltype`='"+soiltype+"',`desp`='"+desp+"' WHERE `id`='"+addcrop+"'"
        cur.execute(sql)
        conn.commit()
        return redirect('viewcrops')
    else:
        return render_template("editcr.html",crop=crop)

@app.route("/deletecr")
def deletecr():
    conn=mysql.connect()
    cursor=conn.cursor()
    addcrop=request.args.get('id')
    cursor.execute("DELETE FROM `addcrop` WHERE `id`='"+addcrop+"'")
    conn.commit()
    return redirect('viewcrops')

@app.route("/viewshare")
def viewshare():
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT `farmerid`,`cropname` FROM `addcrop`")
    data=cursor.fetchall()
    farmerid=[]
    cropname=[]
    
    for i in data:
        cropname.append(i[0])
       
        farmerid.append(i[1])

    
    plt.plot(cropname,farmerid)
    plt.show()
    return redirect('viewcrops')

@app.route("/logout")
def logout():
    return redirect('front')
@app.route("/investor")
def investor():
    conn=mysql.connect()
    cur=conn.cursor()
    cur.execute("SELECT * FROM `addcrop`")
    data=cur.fetchall()
    return render_template("investor.html",todo=data)

@app.route("/view",methods=['GET','POST'])
def view():   
    conn=mysql.connect()
    cursor=conn.cursor()
    addpro=request.args.get('id')
    cursor.execute("SELECT * FROM `addcrop` WHERE `id`='"+addpro+"'")
    pro=cursor.fetchone() 
    if request.method=='POST':
        investorname=request.form['investorname']
        shareamount=request.form['shareamount']
        phone=request.form['phone']
        conn=mysql.connect()
        cur=conn.cursor()
        sql="UPDATE `addcrop` SET `investorname`='"+investorname+"',`shareamount`='"+shareamount+"',`phone`='"+phone+"' WHERE `id`='"+addpro+"'"
        cur.execute(sql)
        conn.commit()
        return redirect('investor')
    else:
        return render_template("view.html",pro=pro)


@app.route("/viewshareinvestor")
def viewshareinvestor():
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT `investorname`,`shareamount` FROM `addcrop`")
    data=cursor.fetchall()
    investorname=[]
    shareamount=[]
    
    for i in data:
        shareamount.append(i[0])
       
        investorname.append(i[1])

    
    plt.plot(shareamount,investorname)
    plt.show()
    return redirect('investor')



@app.route("/front")
def front():        
    return render_template("front.html")

@app.route("/indexa",methods=['GET','POST'])
def indexa():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['pass']
        if username=="admin" and password=="admin":
            return redirect('admin')
    else:
        return render_template("indexa.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/userlist",methods=['GET','POST'])
def userlist():
    conn=mysql.connect()
    cur=conn.cursor()
    cur.execute("SELECT * FROM `register`")
    data=cur.fetchall()
    return render_template("userlist.html",agro=data)

@app.route("/update",methods=['GET','POST'])
def update():
    conn=mysql.connect()
    cursor=conn.cursor()
    addcrop=request.args.get('id')
    cursor.execute("SELECT * FROM `register` WHERE `id`='"+addcrop+"'")
    crop=cursor.fetchone()
    if request.method=='POST':
        name=request.form['name']
        username=request.form['username']
        password=request.form['password']
        address=request.form['address']
        phone=request.form['phone']
        usertype=request.form['usertype']
        conn=mysql.connect()
        cur=conn.cursor()
        sql="UPDATE `register` SET `name`='"+name+"',`username`='"+username+"',`password`='"+password+"',`adddress`='"+address+"',`phone`='"+phone+"',`usertype`='"+usertype+"' WHERE `id`='"+addcrop+"'"
        cur.execute(sql)
        conn.commit()
        return redirect('userlist')
    else:
        return render_template("update.html",crop=crop)

@app.route("/delete")
def delete():
    conn=mysql.connect()
    cursor=conn.cursor()
    addcrop=request.args.get('id')
    cursor.execute("DELETE FROM `register` WHERE `id`='"+addcrop+"'")
    conn.commit()
    return redirect('userlist')
if(__name__=="__main__"):
    app.run(debug=True)