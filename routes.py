import random
import os
from flask_cors import CORS
import flask
from flask_login import login_user, current_user, LoginManager, logout_user
from flask_login.utils import login_required
from models import User, Rating
from wikipedia import get_wiki_link
from tmdb import get_movie_data
from app import app, db

CORS(app)

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_name):
    return User.query.get(user_name)


bp = flask.Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)

RATERS = Rating()


@app.route("/signup")
def signup():
    return flask.render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup_post():
    username = flask.request.form.get("username")
    user = User.query.filter_by(username=username).first()
    if user:
        pass
    else:
        user = User(username=username)
        db.session.add(user)
        db.session.commit()

    return flask.redirect(flask.url_for("login"))


@app.route("/login")
def login():
    return flask.render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    username = flask.request.form.get("username")
    user = User.query.filter_by(username=username).first()
    if user:
        login_user(user)
        return flask.redirect(flask.url_for("index"))

    else:
        return flask.jsonify({"status": 401, "reason": "Username or Password Error"})


MOVIE_IDS = [566525, 370172, 634649, 476669]


@app.route("/rate", methods=["POST"])
def rate():
    data = flask.request.form
    rating = data.get("rating")
    comment = data.get("comment")
    movie_id = data.get("movie_id")

    new_rating = Rating(
        username=current_user.username,
        rating=rating,
        comment=comment,
        movie_id=movie_id,
    )

    db.session.add(new_rating)
    db.session.commit()
    return flask.redirect("index")


@app.route("/")
def landing():
    if current_user.is_authenticated:
        return flask.redirect("index")
    return flask.redirect("login")


@app.route("/logout")
def logout():
    logout_user()
    return flask.redirect("login")


@app.route("/index")
@login_required
def index():
    movie_id = random.choice(MOVIE_IDS)

    # API calls
    (title, tagline, genre, poster_image) = get_movie_data(movie_id)
    wikipedia_url = get_wiki_link(title)

    ratings = Rating.query.filter_by(movie_id=movie_id).all()

    return flask.render_template(
        "index.html",
        title=title,
        tagline=tagline,
        genre=genre,
        poster_image=poster_image,
        wiki_url=wikipedia_url,
        ratings=ratings,
        movie_id=movie_id,
    )


@app.route("/getrates/", methods=["GET", "POST"])
@login_required
def update_rate():
    comments_ = Rating.query.filter_by(username=current_user.username).all()
    comments_data = []
    for comment in comments_:
        comments_data.append(
            {
                "id": comment.id,
                "movie_id": comment.movie_id,
                "username": comment.username,
                "comment": comment.comment,
                "rating": comment.rating,
            }
        )
    return flask.jsonify(comments_data)


@app.route("/deleterates/", methods=["POST"])
@login_required
def delete_rate():
    comments_ = Rating.query.filter_by(username=current_user.username).all()
    comments_data = []
    for comment in comments_:
        comments_data.append(
            {
                "comment": comment.comment,
                "rating": comment.rating,
            }
        )

    db.session.delete(comment)
    db.session.commit()

    return flask.render_template(
        "index.html",
    )


@bp.route("/commentsrates/")
@login_required  # you don't necessarily need this login required line
def getrates():
    # NB: DO NOT add an "index.html" file in your normal templates folder
    # Flask will stop serving this React page correctly
    return flask.render_template("index.html")

    # comment = flask.request.json["comment"]


# rate = flask.request.json["rate"]
# rates.comment = comment
# rates.rate = rate

#  db.session.commit()

#   return RATERS.jsonify(rates)


app.register_blueprint(bp)


if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )
