from flask import Flask, render_template
# flask creates web server
# render_template connect the HTML structure to web server page !

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5002)
