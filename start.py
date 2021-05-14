from flask import Flask, render_template, request
app = Flask(__name__)

from sqlalchemy import create_engine
# create engine is the connection string. This tells you 
# pyslite is a pip package that understands how to talk to sqlite. It translates between sql Alchemy and sql lite: so the order is
# python - sql alchemy - pysqlite - sqllite
# the engine in this case is the object that knows everything and can talk to the database. It's the main thing. 
engine = create_engine("postgresql://a@localhost:5432/RainyDay")

@app.route('/')
def hello_world():
    items=["soso", "du bist also,..", "ein Mensch?"]
    out = render_template("start.html", name="ich bin der grosse weisse elefant. denk an mich.", items=items)
    return out
    
@app.route('/flo')
def flo():
    name = request.args.get("name")
    age=request.args.get("age")
    out = render_template("flo.html", name=name, age=age)
    return out
    
if __name__ == "__main__":
    app.run(debug=True)

