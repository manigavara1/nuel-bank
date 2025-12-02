from flask import Flask
from routes import bp
import config


app = Flask(_name_)
app.register_blueprint(bp)
app.secret_key = config.SECRET_KEY
app.config['SESSION_TYPE'] = 'filesystem'


if _name_ == '_main_':
app.run(host='0.0.0.0', port=5000, debug=True)

