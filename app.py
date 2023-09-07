from flask import Flask, render_template, request
#from geopy.geocoders import Nominatim
from datetime import datetime
from pprint import pprint
import json
from questionaire import CourseForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'shhhhh'

@app.route('/staff_home',methods = ['POST', 'GET'])


@app.route('/', methods=['GET','POST'])
def index():
    questionaire = CourseForm()
    if request.method == 'POST':
        print(questionaire.data)
    return render_template("index.html", form = questionaire)


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

@app.get("/staff_register")
def get_staff_registration():
    return render_template("staff_register.html")

@app.route('/staff_home',methods = ['POST', 'GET'])
def post_staff_registration():
    if request.method == 'POST':
        with open('data/hospitals.json','r+') as hospitals:
            busyness = request.form.get('busyness')
            data = json.load(hospitals)
            for hospital in data:
                if (hospital['name'] == 'Northern Beaches Hospital'):
                    hospital['busyness'] = busyness
            
            hospitals.seek(0)  # rewind
            json.dump(data, hospitals)
            hospitals.truncate()
            
                
                    

    return render_template("staff_home.html")


