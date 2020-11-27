import time
import os

from flask import Flask

app = Flask(__name__)

@app.route("/time")
def get_current_time():
    return {"time": time.time()}

if __name__ == '__main__':

    app.run(
        host=os.environ['SERVER_IP'],
        port=os.environ['SERVER_PORT']
    )