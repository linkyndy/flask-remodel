import rethinkdb as r
from remodel.connection import pool


class Remodel(object):

    def __init__(self, app=None, db=None):
        self.app = app
        self.db = db
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('REMODEL_POOL_SIZE', 5)
        app.config.setdefault('RETHINKDB_HOST', 'localhost')
        app.config.setdefault('RETHINKDB_PORT', '28015')
        app.config.setdefault('RETHINKDB_AUTH', '')
        app.config.setdefault('RETHINKDB_DB', 'test')

        pool.configure(max_connections=app.config['REMODEL_POOL_SIZE'],
                       host=app.config['RETHINKDB_HOST'],
                       port=app.config['RETHINKDB_PORT'],
                       auth_key=app.config['RETHINKDB_AUTH'],
                       db=self.db or app.config['RETHINKDB_DB'])
