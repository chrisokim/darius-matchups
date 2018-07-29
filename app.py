from flask import Flask, render_template

app = Flask(__name__)
#reloads stuff without having to restart
app.debug = True

@app.route('/')
def index():
    #return "test"
    return render_template('home.html')

if __name__ == '__main__':
    app.run()