import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': ""
})

ref = db.reference('Students')

data = {
    
    "852741":
        {
            "name": "B",
            "major": "CS",
            "starting_year": 2022,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
        }
}

for key, value in data.items():
    ref.child(key).set(value)