from flask import Flask, render_template

app = Flask(__name__)


def get_anime():
    return [
        {'id': 1,
         'title': 'Boruto ',
         'rdate': '1945'
         },
        {'id': 2,
         'title': 'Andrew Tate shippuden',
         'rdate': '2023'
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

@app.route('/anime')
def anime():
    animes = get_anime()
    return render_template('anime.html', animes=animes, title='Best Anime')

if __name__ == '__main__':
    app.run()



