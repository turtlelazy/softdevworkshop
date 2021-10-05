from flask import Flask
app = Flask(__name__)  # create instance of class Flask


@app.route("/")  # assign fxn to route
def hello_world():
    #This code does similar to what is done in v3, with the exception of dealing with cases where the file is imported somewhere else
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"



if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
