from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    items=["soso", "du bist also,..", "ein Mensch?"]
    out = render_template("start.html", name="ich bin der grosse weisse elefant. denk an mich.", items=items)
    return out
    
@app.route('/flo')
def flo():
    name = request.args.get("name")
    out = render_template("flo.html", name=name)
    return out
    
if __name__ == "__main__":
    app.run(debug=True)