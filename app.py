from flask import Flask, render_template, request
#from geopy.geocoders import Nominatim
from datetime import datetime
from pprint import pprint
import json
from questionaire import CourseForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'shhhhh'


@app.route('/', methods=['GET','POST'])
def index():
    questionaire = CourseForm()
    if request.method == 'POST':
        print(questionaire.data)
    return render_template("index.html", form = questionaire)

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


