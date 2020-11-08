from flask import render_template, request, flash, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import redirect

from models import *
from app import app,db
from forms import LoginForm, RegisterForm


@app.route('/')
def index_page():
    return render_template("index.html")

@app.route('/login/',methods=['GET','POST','OPTIONS'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate:
        user = User_tbl.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password,form.password.data):
                flash('You have successfully logged in.', "success")
                session['logged_in']=True
                session['email'] = user.email
                session['username'] = user.username
                return redirect(url_for('index_page'))
            flash('Username or Password Incorrect',"Danger")
    return render_template("login.html",form=form)



@app.route('/register/', methods = ['GET', 'POST'])
def register():
    # Creating RegistrationForm class object
    form = RegisterForm(request.form)

    # Cheking that method is post and form is valid or not.
    if request.method == 'POST' and form.validate():

        # if all is fine, generate hashed password
        hashed_password = generate_password_hash(form.password.data, method='sha256')

        # create new user model object
        new_user = User_tbl(

            name = form.name.data,

            username = form.username.data,

            email = form.email.data,

            password = hashed_password )

        # saving user object into data base with hashed password
        db.session.add(new_user)

        db.session.commit()

        flash('You have successfully registered', 'success')

        # if registration successful, then redirecting to login Api
        session['logged_in'] = True
        session['email'] = form.email.data
        session['username'] = form.username.data
        return redirect(url_for('index_page'))

    else:

        # if method is Get, than render registration form
        return render_template('register.html', form = form)


@app.route('/logout/')
def logout():
    # Removing data from session by setting logged_flag to False.
    session['logged_in'] = False
    # redirecting to home page
    return redirect(url_for('index_page'))