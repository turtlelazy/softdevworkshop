# Team FF: Ishraq Mahid and Michelle Lo
# SoftDev
# K19 - A RESTful Journey Skyward/APIs
# November 24th, 2021

from flask import Flask, render_template
import urllib.request, json
app = Flask(__name__)

@app.route("/")
def apod():
    #retrieval and loading of JSON information from apod request to NASA
    page = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=w3dlvp3pigesf9dslufCffVjJUJAoglsX64cF5lK") #opens URL
    dict = json.loads(page.read()) #reads and loads JSON into a python dictionary
    img = dict.get('url') #obtain picture URL through dictionary
    expl = dict.get('explanation') #obtain explanation of image

    # print(dict)
    # print(dict.get('explanation'))
    # print(dict.get('img'))

    return render_template(
        'main.html',
        image = img,
        explanation = expl
    )


@app.route("/random")
def randomApod():
    #retrieval and loading of JSON information from apod request to NASA
    page = urllib.request.urlopen(
        "https://api.nasa.gov/planetary/apod?api_key=w3dlvp3pigesf9dslufCffVjJUJAoglsX64cF5lK&count=1")  # opens URL
    # reads and loads JSON into a python dictionary
    dict = json.loads(page.read())[0] #the returned object from the API is a list -> see count query for apod
    img = dict.get('url')  # obtain picture URL through dictionary
    expl = dict.get('explanation')  # obtain explanation of image

    # print(dict)
    # print(dict.get('explanation'))
    # print(dict.get('img'))

    return render_template(
        'main.html',
        image=img,
        explanation=expl
    )

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
