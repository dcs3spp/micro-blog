from datetime import datetime

from app import create_app, db, cli
from app.models import User, Post, Message, Notification, Task

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "User": User,
        "Post": Post,
        "Message": Message,
        "Notification": Notification,
        "Task": Task,
    }


@app.template_filter("isodatetime")
def jinja2_filter_datetime(dt: datetime):

    return dt.isoformat(" ", "seconds")
