from flask import Flask, render_template  

app = Flask(__name__)

@app.route("/")
def template():
    return render_template("template.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/plot.html")
def plot(): 
    return render_template("plot.html")


@app.route("/links")
def links():
    return render_template("links.html")



@app.route("/map")
def mapview():
    return render_template("mapview.html")
    
if __name__ == "__main__":
    app.run(debug=True)