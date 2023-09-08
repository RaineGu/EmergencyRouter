from flask import Flask, render_template, request, flash, redirect
import json
from geopy.geocoders import Nominatim
from datetime import datetime
from pprint import pprint
import json
from questionaire import CourseForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "shhhhh"


@app.route("/", methods=["GET", "POST"])
def index():
    questionaire = CourseForm()
    if request.method == "POST":
        # Serious cases in which to call an ambulance
        if (
            questionaire.data["airways_compromised"] == "Yes"
            or questionaire.data["breathing_distress"] == "Severe"
            or questionaire.data["breathing_distress"] == "Moderate"
            or len(questionaire.data["blood_circulation"]) > 2
        ):
            flash("This is a medical emergency - Call an ambulance!", "emergency")
            render_template("index.html", form=questionaire)
        else:
            # Calculate estimated priority list and show ER map
            priority = 5  # Lowest ER priority
            symptoms = 1  # Max 10 symptoms to exhibit
            symptoms += len(questionaire.data["blood_circulation"])  # Max 2
            symptoms += len(questionaire.data["dehydration"])  # Max 4

            if questionaire.data["disabilities"] == "Yes":
                symptoms += 1
            if questionaire.data["breathing_distress"] == "Mild":
                symptoms += 1
            if questionaire.data["visibly_pale"] == "Yes":
                symptoms += 1
            if symptoms > 7:
                priority = 3
            elif symptoms > 4:
                priority = 4
            return redirect(f"/map?priority={priority}")
    return render_template("index.html", form=questionaire)


@app.post("/quiz")
def quiz_posted():
    # May need to return a route here? to send a GET request for the map instead of flat returning it?
    return render_template("map.html")


@app.get("/map")
def map():
    # Retrieving data
    priority = request.args.get("priority")
    json_file = open("data\hospitals.json")
    data = json.load(json_file)

    # Creating array of food hospitals
    hospitals = []
    for hospital in data:
        wait = 10 + int(hospital["busyness"]) * int(priority)
        # Adding hospitals to pass into website
        hospitals.append(
            {
                "name": hospital["name"],
                "longitude": hospital["longitude"],
                "latitude": hospital["latitude"],
                "busyness": hospital["busyness"],
                "address": hospital["address"],
                "wait": wait,
            }
        )

    # Getting base device postcode to center map
    # Instantiate a new Nominatim client
    app = Nominatim(user_agent="EmergencyRouter", timeout=40)
    # Get location raw data
    location = app.geocode("The University of New South Wales")
    lat = float(location.latitude)
    long = float(location.longitude)
    return render_template(
        "map.html", hospitals=hospitals, lat=lat, long=long, priority=priority
    )


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


@app.route("/staff_home", methods=["POST", "GET"])
def post_staff_registration():
    if request.method == "POST":
        with open("data/hospitals.json", "r+") as hospitals:
            busyness = request.form.get("busyness")
            data = json.load(hospitals)
            for hospital in data:
                if hospital["name"] == "Northern Beaches Hospital":
                    hospital["busyness"] = int(busyness)

            hospitals.seek(0)  # rewind
            json.dump(data, hospitals)
            hospitals.truncate()

    return render_template("staff_home.html")


@app.get("/admin_login")
def get_admin_login():
    return render_template("admin_login.html")


@app.post("/admin_login")
def post_admin_login():
    return render_template("admin_home.html")
