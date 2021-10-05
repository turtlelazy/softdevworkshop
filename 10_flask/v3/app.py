from flask import Flask
app = Flask(__name__)  # create instance of class Flask


@app.route("/")  # assign fxn to route
def hello_world():
    print("about to print __name__.sldmsdsdsdsddsdsdsslasda... Bismillah")
    print(__name__)  # where will this go?
    #This should go in the terminal, is it did in v2 and v0. However, with a debug variable, perhaps this is only the case when (app.debug).
    #Perhaps if !(app.debug), it won't print anything in terminal at all.

    #When debug was set to true, I saw the print statements as expected. However, if I saved the file and changed it, those changes appeared in terminal and in the website.
    #When debug was set to false, it still printed the statements in the console, but when a change was made it was not put in what was running. When I added random characters and Bismillah,
    #the print statement didn't change. When I added random characters in the return statement, those changes weren't visible either.
    return "No hablo queso! Pero, no es problemawdasdasdsaa"


app.debug = False
app.run()
