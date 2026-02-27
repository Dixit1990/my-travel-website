from flask import Flask, render_template

app = Flask(__name__)

# Example trips data
trips = [
    {
        "id": 1,
        "title": "Munnar, Kerala",
        "region": "India",
        "hero_image": "images/trip1-hero.jpeg",
        "story": "Munnar, in Kerala’s Western Ghats, is renowned for rolling tea plantations, misty hills, waterfalls, and wildlife. A popular retreat offering trekking, lush scenery, and a cool climate.",
        "highlights": [
            "Best time to visit: October - March",
            "Must-see attractions: Solang Valley, Rohtang Pass, Hidimba Temple",
            "Local food to try: Sidu, Trout Fish",
            "Travel tip: Pack warm clothes even in summer!"
        ],
        "photos": [
            "images/trip1/photo-1.jpg",
            "images/trip1/photo-2.jpg",
            "images/trip1/photo-3.jpg",
            "images/trip1/photo-4.jpg",
            "images/trip1/photo-5.jpg",
            "images/trip1/photo-6.jpg",
            "images/trip1/photo-7.jpg",
            "images/trip1/photo-8.jpg"
        ],
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d31425.795163051225!2d77.04357818461045!3d10.080691165374704!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3b0799794d099a6d%3A0x63250e5553c7e0c!2sMunnar%2C%20Kerala%20685612!5e0!3m2!1sen!2sin!4v1772014787226!5m2!1sen!2sin"
    },

    {
        "id": 2,
        "title": "Kochi, Kerala",
        "region": "India",
        "hero_image": "images/trip2-hero.jpeg",
        "story": "Kochi, in Kerala, is a coastal city blending colonial heritage, vibrant culture, and backwaters; nearby hill retreats like Munnar offer tea plantations, cool climate, and scenic views.",
        "highlights": [
            "Best time to visit: November - February",
            "Must-see attractions: Baga Beach, Fort Aguada, Dudhsagar Falls",
            "Local food to try: Goan Fish Curry, Bebinca",
            "Travel tip: Rent a scooter to explore hidden spots."
        ],
        "photos": [
            "images/trip2/photo1.jpg",
            "images/trip2/photo2.jpg",
            "images/trip2/photo3.jpg",
            "images/trip2/photo4.jpg",
            "images/trip2/photo5.jpg",
            "images/trip2/photo6.jpg",
            "images/trip2/photo7.jpg",
            "images/trip2/photo8.jpg"
        ],
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d502958.13718854846!2d75.97243909913463!3d9.987054981985183!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3b080d514abec6bf%3A0xbd582caa5844192!2sKochi%2C%20Kerala!5e0!3m2!1sen!2sin!4v1772015602673!5m2!1sen!2sin"
    },

{
        "id": 3,
        "title": "Kodaikanal, Tamil Nadu",
        "region": "India",
        "hero_image": "images/trip3-hero.jpeg",
        "story": "Kodaikanal is a scenic Tamil Nadu hill station, famed for its cool climate, lush landscapes, lakes, and waterfalls. Popular tourist retreat.",
        "highlights": [
            "Best time to visit: October - March",
            "Must-see attractions: Solang Valley, Rohtang Pass, Hidimba Temple",
            "Local food to try: Sidu, Trout Fish",
            "Travel tip: Pack warm clothes even in summer!"
        ],
        "photos": [
            "images/trip3/photo1.jpg",
            "images/trip3/photo2.jpg",
            "images/trip3/photo3.jpg",
            "images/trip3/photo4.jpg",
            "images/trip3/photo5.jpg",
            "images/trip3/photo6.jpg",
            "images/trip3/photo7.jpg",
            "images/trip3/photo8.jpg"
        ],
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d62821.0367601578!2d77.45712016777094!3d10.236174976988446!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3b0766637f0a0387%3A0x9ffae9373758c13c!2sKodaikanal%2C%20Tamil%20Nadu!5e0!3m2!1sen!2sin!4v1772015666474!5m2!1sen!2sin"
    }
]

@app.route('/')
def home():
    return render_template('index.html', trips=trips)

@app.route('/trip/<int:trip_id>')
def trip_details(trip_id):
    trip = next((t for t in trips if t["id"] == trip_id), None)
    if not trip:
        return "Trip not found", 404
    return render_template('trip.html', trip=trip)

if __name__ == '__main__':
    app.run()
