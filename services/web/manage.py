from flask.cli import FlaskGroup

from api import app, db
from api.mods.users.models.user_model import UserModel


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(UserModel(email="michael@mherman.org", phone="+91-3243243233"))
    db.session.commit()


if __name__ == "__main__":
    cli()
