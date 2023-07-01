from flask import Flask, render_template

app = Flask(__name__)


def get_pets():
    return [
        {'years': 1,
         'name': 'Sara ',
         'animal_type': 'cat'
         },
        {'years': 3,
         'name': 'Jek',
         'animal_type': 'dog'
         }
    ]

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/<string:name>')
def hey_name(name: str):
    return render_template('hello.html', title=name.capitalize(), nameForHTML=name.capitalize())

@app.route('/pets')
def anime():
    pets = get_pets()
    return render_template('pets.html', pets=pets, title='My pets')

if __name__ == '__main__':
    app.run()



