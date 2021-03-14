from flask import Flask
import click

from flask.cli import with_appcontext

from flask_sqlalchemy import SQLAlchemy

'sqlite:///marketshop.db'

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketshop.db'
    app.config['SQLALCHEMYY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.cli.add_command(init_db_command)

    with app.app_context():
        from . import routes
    return app


@click.command('init-db')
@with_appcontext
def init_db_command():
    from . import entidades
    db.create_all()
    click.echo('Voce conseguiu cara!!')