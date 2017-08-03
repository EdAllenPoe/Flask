from flask import Flask
app=Flask(__name__)

@app.route('/')

def howdy_everyone():
    return "Howdy Everyone!!"

app.run(debug=True)
