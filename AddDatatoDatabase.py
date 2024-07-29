import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendacerealtime-90713-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "211160":
        {
            "name": "Shreya Singh Rathore",
            "major": "CSE",
            "starting_year": 2021,
            "total_attendance": 5,
            "standing": "A",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "211041":
        {
            "name": "Ashutosh Rathore",
            "major": "CSE",
            "starting_year": 2021,
            "total_attendance": 5,
            "standing": "B",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "211042":
        {
            "name": "Asmi Anand",
            "major": "CSE",
            "starting_year": 2021,
            "total_attendance": 5,
            "standing": "C",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)





