from flask import Flask
app = Flask(__name__)  # create instance of class Flask


@app.route("/")  # assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)  # where will this go?
    #It should go to the same place as it did in v0, in the terminal at the beginning, but this time after "about to print __name__"
    #Output occurred as predicted
    return "No hablo queso!"


app.run()
