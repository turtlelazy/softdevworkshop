"""
Ishraq Mahid, Lucas Tom-Wong (LTW), Tomas Acuna
SoftDev
K14 -- Form and Function -- Utilizing Request Info
2021-10-15
"""

from flask import Flask  # facilitate flask webserving
from flask import render_template  # facilitate jinja templating
from flask import request
from flask.helpers import make_response  # facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)  # create Flask object


@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    """
    renders the login page
    """
    return render_template('login.html')
    #brings up the login.html page
    #askes for inputs of a text and to press a submit button


@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    """
    renders response template, placing in the username and method retrieved from the request
    """
    return render_template('response.html', username=request.args.get('username'), method=request.method)
    #brings up the response.html page with username and the method request sent to the page
    #uses responses from previous inputs/method


if __name__ == "__main__":  
    """
    false if this file imported as module
    debugging enabled    
    """
    app.debug = True
    app.run()
