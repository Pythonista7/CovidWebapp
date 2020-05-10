from flask import Flask, render_template  
import helper

app = Flask(__name__)

@app.route("/")
def template():
    return render_template("template.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/ward/<no>")
def ward_info(no):
    c_map=helper.Covid_Mapper()
    c_map.get_ward_info(no)
    return render_template("ward_info.html",context=c_map.get_ward_info(no))

@app.route("/plot/<dist_no>")
def plt_view(dist_no='all'):
    if dist_no=='all':
        return render_template("plot.html")
    else:
        return "under dev"

@app.route('/plot')
def plot():
    return render_template("plot")

@app.route("/links")
def links():
    return render_template("links.html")


@app.route("/map/<day>")
def kp_view(day):
    c_map=helper.Covid_Mapper()
    c_map.get_for_day(day)
    return render_template("serve.html")

@app.route("/mapview")
def mapview():
    return render_template('mapview.html')

if __name__ == "__main__":
    app.run(debug=True)