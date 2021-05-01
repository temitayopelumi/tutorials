from flask import Flask, render_template

# creates a Flask application, named app
app = Flask (__name__)


# a route where we will display a welcome message via an HTM
@app.route ("/")
def main ():
    return render_template ('main.html')


# run the application
if __name__ == "__main__":
    app.run ()
