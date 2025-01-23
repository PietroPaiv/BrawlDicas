from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/brawlers')
def brawlers():
    return render_template('brawlers.html')

@app.route('/modos')
def modos():
    return render_template('modos.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

if __name__ == '__main__':
    app.run(debug=True)
