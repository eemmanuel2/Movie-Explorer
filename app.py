# pylint: disable=warning codes, warnings code, more warnings codes
import os
import flask
from dotenv import load_dotenv, find_dotenv
from flask_login import LoginManager, login_user, current_user, logout_user, UserMixin
from flask_sqlalchemy import SQLAlchemy
from tmdb import movie_id_search
import random


load_dotenv(find_dotenv())  # This is to load your API keys from .env


app = flask.Flask(__name__)

db = SQLAlchemy()
db.init_app(app)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("database_URL")
# Gets rid of a warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


login_manager = LoginManager()  # Create a Login Manager instance
login_manager.login_view = "auth.login"  # define the redirection path when login required and we attempt to access without being logged in
login_manager.init_app(app)  # configure it for login


@login_manager.user_loader
def load_user(user_id):  # reload user object from the user ID stored in the session
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    """User model"""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return "<User {self.id}>"


class Rating(db.Model):
    """Rating in ratings database"""

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rating = db.Column(db.Integer, default=0)
    comment = db.Column(db.String(), nullable=False)
    m_id = db.Column(db.Integer, default=0)


with app.app_context():
    db.create_all()


@app.route("/login", methods=["GET", "POST"])  # define login page path
def login():  # define login page fucntion
    if (
        flask.request.method == "GET"
    ):  # if the request is a GET we return the login page
        return flask.render_template("login.html")
    else:  # if the request is POST the we check if the user exist and with te right password
        username = flask.request.form.get("username")
        user = User.query.filter_by(username=username).first()
        # check if the user actually exists
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        if not user:
            flask.flash("Please sign up before you try to rate!")
            return flask.redirect(flask.url_for("login"))

        # if the above check passes, then we know the user has the right credentials
        login_user(user)
        return flask.redirect(flask.url_for("ratecard"))


@app.route("/ratecard", methods=["GET", "POST"])
def ratecard():
    movies1 = [566525, 370172, 634649, 476669, 351346]
    a = random.randrange(0, len(movies1) - 1)
    movie_id = movies1[a]
    movie_search = movie_id_search()

    if flask.request.method == "POST":

        #   ratg = flask.request.form.get("rating")
        #   cmmnt = flask.request.form.get("comment")
        #   db.session.add(cmmnt)
        #   db.session.add(ratg)
        #   db.session.commit()
        data = flask.request.form
        rate = data["rating"]

        comnt = data["comment"]
        record = Rating(rating=rate, comment=comnt, m_id=movie_id)
        db.session.add(record)
        db.session.commit()

    rates = Rating.query.all()
    num_rates = len(rates)
    comments = Rating.query.all()
    num_comments = len(comments)
    return flask.render_template(
        "ratecard.html",
        moviename=movie_search["moviename"],
        movietag=movie_search["movietag"],
        moviepicture=movie_search["moviepicture"],
        moviegenre=movie_search["moviegenre"],
        piclink=movie_search["piclink"],
        wiki=movie_search["wiki"],
        movi_id=movie_search["movi_id"],
        rates=rates,
        num_rates=num_rates,
        num_comments=num_comments,
        comments=comments,
    )


@app.route("/", methods=["GET", "POST"])
def signup():  # define the sign up function
    if (
        flask.request.method == "GET"
    ):  # If the request is GET we return the sign up page and forms
        return flask.render_template("index.html")
    else:  # if the request is POST, then we check if the email doesn't already exist and then we save data

        username = flask.request.form.get("username")

        user = User.query.filter_by(
            username=username
        ).first()  # if this returns a user, then the email already exists in database
        if (
            user
        ):  # if a user is found, we want to redirect back to signup page so user can try again
            flask.flash("user already exists")
            return flask.redirect(flask.url_for("login"))
        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        new_user = User(username=username)  #
        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()
        return flask.redirect(flask.url_for("login"))


app.run(
    host=os.getenv("IP", "0.0.0.0"),
    port=int(os.getenv("PORT", 8080)),
)
