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
    
    """
    foo = website heading
    header = h1 tag
    names = trio names
    occ = random occupation
    coll is taken from occupations.py, it is essentially a dictionary being passed on
    """

    currentOccupation = occupations.chooseRandom()
    firstWord = currentOccupation.partition(' ')[0]
    wikipediaPage = "https://en.wikipedia.org/wiki/" + firstWord

    return render_template('tablified.html', 
        foo="Occupations", 
        header = "Data Covering Various Occupations and their Respective Percentages", 
        names = "Gitsters | Alejandro Alonso, Ivan Lam, Ishraq Mahid",
        occ = currentOccupation,
        wiki = wikipediaPage
,       
        collection=coll)

if __name__ == "__main__":
    app.debug = True
    app.run()
