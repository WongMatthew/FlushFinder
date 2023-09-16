from flask import Flask, request
import json
import os


# https://flask.palletsprojects.com/en/2.3.x/quickstart/#about-responses

app = Flask(__name__)

"""
Get a single washroom -- modal
"""
@app.get("/washroom/<wid>")
def washroom_qeury():
    req = request.json

    # pass washroom id to query for washroom profile in DB
    # TODO

    # deserialize the washroom object
    response = json.dumps()
    return response

"""
Get list of (all) washrooms -- map
"""
@app.get("/washroom/all")
def all_washrooms():
    req = request.json

    # fetch all
    # TODO


    # deserialize into list of washroom objects
    response = json.dumps()
    return response


"""
Create a washroom submission request

Update a washroom submission
- status field indicating status of submission
- "pending" -> 0 , "approved" -> 1, "rejected" -> 2
"""
@app.route("/submission/", methods=["POST", "PUT"])
def submissions():
    req = request.json

    # make request object and pass into db orm
    # TODO
    if request.method == "POST":
        pass

    # query request db for washroom id, update status col
    # TODO
    else:
        if request.form['status'] == 1:
            # update the request db, remove approved requests?
            # create new row in washroom db
            pass
        elif request.form['status'] == 2:
            # remove the washroom submission?
            pass

    return "OK"


"""
Get all washroom submission requests
"""
@app.get("/submission/all")
def all_submissions():
    # TODO
    return "OK"


"""
base of controller 
"""
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run()