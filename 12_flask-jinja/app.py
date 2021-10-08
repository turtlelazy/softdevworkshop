# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

# Q0: What happens if you remove render_template from this line?
#Nothing happens to the root directory. But it would cause an error on 
# /my_foist_template, because the template can't be rendered

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

@app.route("/my_foist_template") #Q1: Can all of your teammates confidently predict the URL to use to load this page?
#Yes. We've realized that this keyword specifies the directory, with root being at /
def test_tmplt():
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll) #Q2: What is the significance of each argument?
    #They look like parameters to this function called render_template. 
    #We specify the target template, and set variables equal to what we want.
    #The template itself has spots for the foo and collection variables, 
    #and it appears almost as if that spot is translated by Flask for it's own purposes.

if __name__ == "__main__":
    app.debug = True
    app.run()
