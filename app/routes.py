from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/galeria')
def getGallery():
    galeria = [
        'https://data.whicdn.com/images/26217082/large.jpg'
        'http://www.goodwp.com/large/201111/20430.jpg'
        'https://animalcafes.com/pix/800-hara-bengal.jpg'
        'https://www.gregdutoit.com/i/ForestLion_ForestHorizontal_Thumbnail.jpg'
    ]

    return render_template('galeria.html', galeria=galeria)

