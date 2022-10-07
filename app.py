from flask import Flask


app = Flask(__name__)

@app.get("/")
def pokemon_list():
    return "Charmander, pikachu , eveee, bulbasaur, diglett"

@app.get("/bulbasaur")
def bulbasaur_data():
    return "This is bulbasaur, a generation 1 pokemon who looks like a little dinosaur"

@app.get("/charmander")
def charmander_data():
    return "This is charmander, a generation 1 pokemon who looks like a little dinosaur"

@app.get("/eveee")
def eveee_data():
    return "This is eveee, a generation 1 pokemon who looks like a little rodent"

@app.get("/diglett")
def diglett_data():
    return "This is diglett, a generation 1 pokemon who looks like a little rodent"

if __name__ == "__main__":
    app.run()