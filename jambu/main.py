import os

from paste.deploy import loadapp
from waitress import serve

if __name__ == "__main__":
    print("hi!")
    port = int(os.environ.get("PORT", 2300))
    app = loadapp('config:development.ini', relative_to='.')

    serve(app, host='0.0.0.0', port=port)