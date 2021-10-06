"""
Cool Dogs - Ishraq Mahid & Fish, Ivan Mijacika & Bob, and Gavin McGinley & Craig
SoftDev
k10 -- Flask Greatness -- Exploration of Flask framework -- We explored written code to understand flask and created our own code
2021 - 10 - 4


"""
from flask import Flask
from randomOcc06 import weighted
from randomOcc06 import generateListStr

app = Flask(__name__)  # create instance of class Flask
tnpg = "<h1>Cool Dogs - Ishraq Mahid & Fish, Ivan Mijacika & Bob, and Gavin McGinley & Craig</h1>"

@app.route("/")  # assign fxn to route

def hello_world():
    #This code does similar to what is done in v3, with the exception of dealing with cases where the file is imported somewhere else
    print("the __name__ of this module is... ")
    print(__name__)
    job = weighted()
    return tnpg + "<img src = 'https://media1.giphy.com/media/1lBjBpMwgI8PBZKov0/giphy.gif?cid=790b761143d782cb33450122ff9ea261bb48f236bc68b9fe&rid=giphy.gif&ct=g'>"+"<h2>" + job + "</h2>" + generateListStr(job)


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
