from methods import userDetails, convertUnixTime, getTags, contestDetails
from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html",give_error=False)

@app.route("/login",methods=["GET","POST"])
def login():
    userInfo = False
    if request.method=="POST":
        user=request.form['username']
    userInfo = userDetails(user, False)
    if(userInfo == False):
        return render_template('login.html',give_error=True)
    if 'rating' not in userInfo:
        return render_template('login.html',usererror=True)
    dt_object = convertUnixTime(userInfo['lastOnlineTimeSeconds'])

    weakTags = getTags(userInfo['handle'], userInfo['rating'])

    return render_template('profile.html', user=userInfo, lastOnline=dt_object, tags= weakTags)

@app.route("/contests",methods=["GET","POST"])
def contests():
    contestsList = contestDetails()
    return render_template('future_contests.html', contests= contestsList)

if __name__=="__main__":
    app.run(debug=True)