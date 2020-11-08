from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '~\xb4!|3\xaf\xc3\xf5\xee"V\xc3|+\x97\xc5'
# postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@localhost:5432/flask_ed_dash'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy(app)
migrate =Migrate(app, db)
# from models import *
from views import *


if __name__ == '__main__':
	app.run(debug=True)

