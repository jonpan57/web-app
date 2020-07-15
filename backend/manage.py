from app import create_app
from flask_script import Manager, Shell, Server

import config

app = create_app(config)
manager = Manager(app)
