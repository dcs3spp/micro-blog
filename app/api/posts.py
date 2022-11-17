from flask import current_app, flash, redirect, render_template, request, url_for
from flask_babel import _
from flask_login import current_user, login_required
from app import db
from app.api import bp
from app.main.forms import PostForm
from app.models import Post


@bp.route("/post", methods=["GET", "POST"])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = form.post.data
        language = request.accept_languages.best_match(current_app.config["LANGUAGES"])
        new_post = Post(body=post, author=current_user, language=language)
        db.session.add(new_post)
        db.session.commit()
        flash(_("Your post has been saved."))
        return redirect(url_for("main.explore"))
    elif request.method == "GET":
        return render_template("edit_profile.html", title=_("New Post"), form=form)
