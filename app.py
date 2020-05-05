import config
from apis import api
from flask import Flask

app = Flask(__name__)
api.init_app(app)

if __name__ == '__main__':
    app.config.from_object('config')
    app.run(port=config.PORT_NUMBER)