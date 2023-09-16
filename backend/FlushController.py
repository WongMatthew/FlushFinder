from flask import Flask
app = Flask(__name__)

"""
Get a single washroom 
"""


"""
Get list of (all) washrooms
"""


"""
Create an (approved) washroom profile
"""


"""
Create a washroom submission 
"""


"""
base of FlushController
"""
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run()
