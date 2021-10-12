# Gitsters: Alejandro Alonso, Ivan Lam, Ishraq Mahid
# SoftDev
# K13 -- Template for Success
# 2021-10-08

#Initial setup
import occupations
from flask import Flask, render_template
app = Flask(__name__)

coll = occupations.init()
@app.route("/occupyflaskst")
def test_tmplt():

    return render_template('tablified.html', 
        #foo is the website heading
        foo="Occupations", 
        #header is the h1 tag
        header = "Data Covering Various Occupations and their Respective Percentages", 
        #Names is our trio
        names = "Gitsters | Alejandro Alonso, Ivan Lam, Ishraq Mahid",
        #occ is a random occupation
        occ = occupations.chooseRandom()
,       #taken from occupations.py, it is essentially a dictionary being passed on
        collection=coll)

if __name__ == "__main__":
    app.debug = True
    app.run()
