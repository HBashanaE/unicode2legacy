from flask import Flask

from core.UnicodeToLegacy import unicodeToLegacyBP
from home.Home import homeBP

app = Flask(__name__)
app.register_blueprint(unicodeToLegacyBP, url_prefix='/convert')
app.register_blueprint(homeBP, url_prefix='/')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
