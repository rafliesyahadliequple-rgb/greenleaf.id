from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/katalog')
def katalog():
    return render_template('katalog.html')
@app.route('/tips')
def tips():
    return render_template('tips.html')
@app.route('/kontak')
def kontak():
    return render_template('kontak.html')

if __name__ == '__main__':
    app.run(debug=True)

