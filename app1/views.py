from django.shortcuts import render
from datetime import date

# Post Details As we dont use Database
all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": """Embarking on a journey into the mountains is an enchanting odyssey, where each step is a dance with nature's elements. The towering peaks, crisp mountain air, and the serenity that envelopes you create an experience that transcends the physical act of hiking. It's a transformative adventure that connects you with the essence of the mountains—a call that beckons adventurers to explore the rugged landscapes and discover the magic within.""",
        "content": "Hiking in the mountains is a transformative experience that challenges the body and invigorates the spirit. The climb, whether navigating winding trails, crossing babbling streams, or ascending steep slopes, becomes a triumph over nature's challenges. The reward lies not just in reaching the summit but in the journey itself, where every step unveils breathtaking vistas and allows communion with nature. The mountains offer solitude and reflection, a chance to disconnect from the hustle of daily life and reconnect with one's inner self. Beyond the physical exertion, hiking in the mountains leaves an indelible mark—a renewed connection with nature and a piece of oneself discovered along the trail. So, lace up your boots, answer the call of the mountains, and let the transformative magic of hiking guide you to new heights",
    },
    {
        "slug": "sky-diving",
        "image": "sky.jpg",
        "date": date(2022, 4, 11),
        "title": "Sky Diving",
        "excerpt": """ Plummeting from the heavens, skydiving is not merely an adrenaline-pumping sport; it's a visceral dance with the skies, a journey that defies gravity and challenges the limits of human courage. In those fleeting moments of free fall, the world below becomes a blur, and the wind's embrace becomes a tangible force. Skydiving is a symphony of fear and exhilaration, a daring act that transforms not only the landscape below but the very fabric of the skydiver's soul.""",
        "content": "Skydiving is an unparalleled adventure that thrusts participants into the exhilarating realm between Earth and sky. The experience begins with the heart-pounding ascent to altitude, a moment of anticipation as the plane climbs higher, carrying both excitement and nervous energy. In those breathtaking seconds of free fall, skydivers experience a unique sensation of weightlessness, a feeling of liberation that transcends the ordinary.",
    },
    {
        "slug": "scuba-diving",
        "image": "scuba.jpg",
        "date": date(2020, 3, 19),
        "title": "Scuba Diving",
        "excerpt": """Scuba diving is a mesmerizing exploration of the mysterious depths beneath the ocean's surface, where gravity seems to lose its grip, and a vibrant underwater world comes to life. It's an adventure that transcends the boundaries of land, immersing divers in a surreal realm of marine life, coral formations, and submerged landscapes. The allure of scuba diving lies not only in the thrill of the descent but in the opportunity to witness the ocean's breathtaking biodiversity up close.""",
        "content": "Scuba diving is a unique and exhilarating activity that requires training, skill, and a deep respect for the ocean's ecosystems. From the vibrant coral reefs of tropical seas to the hauntingly beautiful kelp forests in cooler waters, each dive presents an opportunity to witness the diverse and intricate tapestry of marine life. Divers often find themselves in awe as they encounter schools of colorful fish, graceful sea turtles, and majestic creatures like rays and sharks, creating indelible memories of the wonders hidden beneath the surface of the world's oceans.",
    },
    {
        "slug": "bungee-jumping",
        "image": "jumping.jpg",
        "date": date(2023, 2, 15),
        "title": "Bunjee Jumping",
        "excerpt": """Bungee jumping is the epitome of adrenaline-fueled adventure, a daring leap into the abyss that defies gravity and sends pulses racing. It's not merely a sport but a visceral experience that challenges the boundaries of fear, inviting participants to confront the void below. The allure of bungee jumping lies in the sheer thrill of free fall and the exhilaration of rebounding skyward, creating an unforgettable dance between the jumper and the forces of gravity.""",
        "content": "Bungee jumping, with its origins rooted in ancient rites of passage, has evolved into a global phenomenon that attracts thrill-seekers seeking the ultimate adrenaline rush. The experience typically involves a leap from a platform or a bridge, secured by an elastic cord that propels the jumper into a heart-pounding free fall before rebounding. Beyond the physical rush, bungee jumping is a test of mental fortitude, requiring participants to overcome fear and embrace the liberating sensation of defying gravity. Each jump becomes a moment of personal triumph, a visceral encounter with the unknown, and a lasting memory etched in the minds of those who take the plunge into the abyss.",
    },
    {
        "slug": "river-rafting",
        "image": "rafting.jpg",
        "date": date(2019, 3, 23),
        "title": "River Rafting",
        "excerpt": """River rafting is an exhilarating aquatic escapade that beckons adventurers to navigate the untamed currents, where the thrill of white-water rapids meets the serenity of pristine landscapes. It's a dynamic fusion of teamwork, adrenaline, and nature's raw power, weaving a narrative of excitement that unfolds with each twist and turn of the river. River rafting isn't just a sport; it's a pulse-pounding journey that immerses participants in the heart of some of the world's most breathtaking and challenging waterways.""",
        "content": "River rafting, often regarded as a communal sport, requires a coordinated effort among a team of rafters to navigate the varying degrees of rapids and obstacles. From the meandering stretches that allow for scenic appreciation to the heart-pounding tumult of frothy rapids, each segment of the river offers a unique adventure. As paddlers work in unison to conquer the twists and turns, the experience becomes a harmonious dance with nature's forces. River rafting not only provides an adrenaline rush but also fosters a deep connection with the water and the landscapes it courses through, creating memories of camaraderie and triumph in the face of the river's untamed spirit.",
    },
]

# Helper Functions

def get_date(post):
    return post['date']
# Create your views here.


def homePage(request):
    # 4 latest post 
    sorted_posts = sorted(all_posts,key = get_date)
    sorted_posts = sorted_posts[-4:]
    return render(request, "app1/index.html",{
        "posts" : sorted_posts
    })


def post(request):
    return render(request, "app1/all-posts.html",{
        "posts" : all_posts
    })


def detailPost(request, slug):
    # check slug in dictionary
    requiredPost = None
    for post in all_posts:
        if post['slug'] == slug:
            requiredPost = post
            break
    
    if requiredPost != None:
        return render(request, "app1/post-detail.html",{
            "post" : requiredPost
        })
