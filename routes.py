from datetime import timedelta

from flask import Flask, flash, redirect, render_template, session, url_for
from flask_bcrypt import Bcrypt, check_password_hash, generate_password_hash
from flask_login import (LoginManager, UserMixin, current_user, login_required,
                         login_user, logout_user)
from sqlalchemy.exc import (DatabaseError, DataError, IntegrityError,
                            InterfaceError, InvalidRequestError)
from werkzeug.routing import BuildError

from app import create_app, bcrypt, db, login_manager
from forms import login_form
from UserDBAPI import Account


@login_manager.user_loader
def load_user(user_id):
    return Account.query.get(int(user_id))

app = create_app()

@app.before_request
def session_handler():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1)

@app.route("/", methods=("GET", "POST"), strict_slashes=False)
def index():
    print('Hi')
    return render_template("index.html",title="Home")


@app.route("/auth/", methods=("GET", "POST"), strict_slashes=False)
def login():
    form = login_form()

    if form.validate_on_submit():
        try:
            user = Account.query.filter_by(email=form.email.data).first()
            if check_password_hash(user.pwd, form.pwd.data):
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash("Invalid Username or password!", "danger")
        except Exception as e:
            flash(e, "danger")

    return render_template("auth.html",
        form=form,
        text="Login",
        title="Login",
        btn_action="Login"
        )


if __name__ == "__main__":
    app.run(debug=True)
