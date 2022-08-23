from flask import Flask
from views import views

app = Flask(__name__)


app.register_blueprint(views, url_prefix="/views")


if __name__ == '__main__':
    app.run(port=8000) #debug=True automatically rerun whenever you make any change
