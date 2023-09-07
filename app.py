from flask import Flask, render_template, request
#from geopy.geocoders import Nominatim
from datetime import datetime
from pprint import pprint
from questionaire import CourseForms

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.post("/")
def quiz_posted():
    # May need to return a route here? to send a GET request for the map instead of flat returning it?
    return render_template("map.html")

@app.get("/map")
def map():
    return render_template("map.html")

@app.get("/register_hospital")
def get_registration():
    return render_template("register_hospital.html")

@app.post("/register_hospital")
def post_registration():
    return render_template("index.html")

@app.get("/staff_login")
def get_staff_login():
    return render_template("staff_login.html")

@app.post("/staff_login")
def post_staff_login():
    return render_template("staff_home.html")

#@app.get("/staff_register")
#def get_staff_registration():
#    return render_template("staff_register.html")

@app.get("/staff_register")
def post_staff_registration():
    return render_template("staff_home.html")

@app.get("/admin_login")
def get_admin_login():
    return render_template("admin_login.html")

@app.post("/admin_login")
def post_admin_login():
    return render_template("admin_home.html")
