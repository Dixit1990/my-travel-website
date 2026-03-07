from flask import Flask, render_template

app = Flask(__name__)

# Example trips data
trips = [
    {
        "id": 1,
        "title": "Munnar",
        "region": "Kerala",
        "hero_image": "images/trip1-hero.jpeg",
        "story": "Munnar, in Kerala’s Western Ghats, is renowned for rolling tea plantations, misty hills, waterfalls, and wildlife. A popular retreat offering trekking, lush scenery, and a cool climate.",
        "highlights": [
            "Best time to visit: Aug-Dec",
            "Must-see attractions: Tea Museum, Botanical Garden, Fun Forest",
            "Local food to try: ",
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
        "title": "Kochi",
        "region": "Kerala",
        "hero_image": "images/trip2-hero.jpeg",
        "story": "Kochi, in Kerala, is a coastal city blending colonial heritage, vibrant culture, and backwaters; nearby hill retreats like Munnar offer tea plantations, cool climate, and scenic views.",
        "highlights": [
            "Best time to visit: November - February",
            "Must-see attractions: Baga Beach, Fort Aguada, Dudhsagar Falls",
            "Local food to try: Goan Fish Curry, Bebinca",
            "Travel tip: Rent a scooter to explore hidden spots."
        ],
        "photos": [
            "images/trip2/photo-1.jpg",
            "images/trip2/photo-2.jpg",
            "images/trip2/photo-3.jpg",
            "images/trip2/photo-4.jpg",
            "images/trip2/photo-5.jpg",
            "images/trip2/photo-6.jpg",
            "images/trip2/photo-7.jpg",
            "images/trip2/photo-8.jpg"
        ],
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d502958.13718854846!2d75.97243909913463!3d9.987054981985183!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3b080d514abec6bf%3A0xbd582caa5844192!2sKochi%2C%20Kerala!5e0!3m2!1sen!2sin!4v1772015602673!5m2!1sen!2sin"
    },

{
        "id": 3,
        "title": "Kodaikanal",
        "region": "Tamil Nadu",
        "hero_image": "images/trip3-hero.jpeg",
        "story": "Kodaikanal is a scenic Tamil Nadu hill station, famed for its cool climate, lush landscapes, lakes, and waterfalls. Popular tourist retreat.",
        "highlights": [
            "Best time to visit: October - March",
            "Must-see attractions: Coakers walk, Lake viewpoint, Pine forest, Guna Cave",
            "Local food to try: Idly & Sambhar",
            "Travel tip: Pack warm clothes even in summer!"
        ],
        "photos": [
            "images/trip3/photo-1.jpg",
            "images/trip3/photo-2.jpg",
            "images/trip3/photo-3.jpg",
            "images/trip3/photo-4.jpg",
            "images/trip3/photo-5.jpg",
            "images/trip3/photo-6.jpg",
            "images/trip3/photo-7.jpg",
            "images/trip3/photo-8.jpg"
        ],
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d62821.0367601578!2d77.45712016777094!3d10.236174976988446!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3b0766637f0a0387%3A0x9ffae9373758c13c!2sKodaikanal%2C%20Tamil%20Nadu!5e0!3m2!1sen!2sin!4v1772015666474!5m2!1sen!2sin"
    },
{
        "id": 4,
        "title": "Valparai",
        "region": "Tamil Nadu",
        "hero_image": "images/trip4-hero.jpeg",
        "story": "Misty tea estates, winding mountain roads, hidden waterfalls, and wildlife sightings make Valparai a peaceful paradise deep inside the Western Ghats.",
        "highlights": [
            "Best time to visit: Jul-Dec",
            "Must-see attractions: Sholayar Dam, Monkey falls, Nallamudi viewpoint, Balaji Temple",
            "Local food to try: Filter coffee, Masala Dosa, Fresh Tea",
            "Travel tip: Pack warm clothes even in summer!"
        ],
        "photos": [
            "images/trip4/photo-1.jpg",
            "images/trip4/photo-2.jpg",
            "images/trip4/photo-3.jpg",
            "images/trip4/photo-4.jpg",
            "images/trip4/photo-5.jpg",
            "images/trip4/photo-6.jpg",
            "images/trip4/photo-7.jpg",
            "images/trip4/photo-8.jpg"
        ],
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d31401.490239763898!2d76.93479697062038!3d10.326972546908587!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3ba8279db1aa1b0f%3A0x86bc2b6e18667469!2sValparai%2C%20Tamil%20Nadu%20642127!5e0!3m2!1sen!2sin!4v1772855677362!5m2!1sen!2sin"
    },

{
        "id": 5,
        "title": "Athirapally Waterfalls",
        "region": "Tamil Nadu",
        "hero_image": "images/trip5-hero.jpeg",
        "story": "The majestic Athirappilly Waterfalls roars through lush forests, earning its title as the “Niagara of India” in Kerala’s scenic Western Ghats.",
        "highlights": [
            "Best time to visit: Jul-Dec",
            "Must-see attractions: Vazhachal waterfalls, Charpa waterfalls, Chalakudy river",
            "Local food to try: Filter coffee, Masala Dosa, Fresh Tea",
            "Travel tip: Pack warm clothes in winter!"
        ],
        "photos": [
            "images/trip5/photo-1.jpg",
            "images/trip5/photo-2.jpg",
            "images/trip5/photo-3.jpg",
            "images/trip5/photo-4.jpg",
            "images/trip5/photo-5.jpg",
            "images/trip5/photo-6.jpg",
            "images/trip5/photo-7.jpg",
            "images/trip5/photo-8.jpg"
        ],
        "map_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3925.7098535606237!2d76.56686917366083!3d10.284945789835497!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3b07f923c2abb0d1%3A0x1e7af75aa13af78!2sAthirappilly%20Water%20Falls!5e0!3m2!1sen!2sin!4v1772877695133!5m2!1sen!2sin"
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
