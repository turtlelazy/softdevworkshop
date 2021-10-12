# Gitsters: Alejandro Alonso, Ivan Lam, Ishraq Mahid
# SoftDev
# K13 -- Template for Success
# 2021-10-08

import occupations
from flask import Flask, render_template
app = Flask(__name__)

coll = occupations.init()
occupation = occupations.chooseRandom()

@app.route("/occupyflaskst")
def test_tmplt():
    return render_template('tablified.html', 
        foo="Occupations", 
        header = "Data Covering Various Occupations and their Respective Percentages", 
        names = "Gitsters | Alejandro Alonso, Ivan Lam, Ishraq Mahid",
        occ = occupation,
        collection=coll)

if __name__ == "__main__":
    app.debug = True
    app.run()
