from flask import Flask, render_template

app = Flask(__name__)

### Web Pages ###
@app.route("/", methods=['GET','POST'])
def home():
    return render_template("index.html")

@app.route("/superlatives", methods=['GET','POST'])
def superlatives():
    return render_template("superlatives.html")

@app.route("/timeseries", methods=['GET','POST'])
def time_series():
    return render_template("time_series.html")

@app.route("/textual", methods=['GET','POST'])
def textual():
    return render_template("textual.html")

if __name__ == '__main__':
    app.run(debug=True)
