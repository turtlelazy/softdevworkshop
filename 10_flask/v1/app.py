from flask import Flask
app = Flask(__name__)  # create instance of class Flask


@app.route("/")  # assign fxn to route
def hello_world():
    return "No hablo queso!" 
    #It should simply output "No hablo queso!" to the website, but this time it won't print anything to the terminal
    #The output matched as predicted


app.run()
