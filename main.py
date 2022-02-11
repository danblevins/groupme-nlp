from flask import Flask, render_template

app = Flask(__name__)

### Web Pages ###
@app.route("/", methods=['GET','POST'])
def home():
    return render_template("index.html")

@app.route("/superlatives", methods=['GET','POST'])
def superlatives():
    return render_template("superlatives.html")

if __name__ == '__main__':
    app.run(debug=True)
