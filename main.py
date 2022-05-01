from flask import Flask, render_template,url_for

app = Flask(__name__)


@app.route("/")
def home():
    # return "<p>Hello, World!</p>"
    return render_template('index.html')
@app.route('/submit',methods=['POST','GET'] )
def submit():
    # return "<p>Hello, World!</p>"
    return render_template('asd.html')
if __name__ == "__main__":
    app.run(debug=True)
