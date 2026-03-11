from flask import Flask, render_template
import json

app = Flask(__name__)

def load_trips():
    with open("trips.json", "r") as file:
        return json.load(file)

@app.route('/')
def home():
    trips=load_trips()
    return render_template('index.html', trips=trips)

@app.route('/trip/<int:trip_id>')
def trip_details(trip_id):
    trips=load_trips()
    trip = next((t for t in trips if t["id"] == trip_id), None)
    if not trip:
        return "Trip not found", 404
    return render_template('trip.html', trip=trip)

if __name__ == '__main__':
    app.run()
