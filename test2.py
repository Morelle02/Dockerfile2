from flask import Flask

app = Flask(_name_)

@app.route('/')
def get_prenom():
    # Le prénom que vous voulez retourner
    prenom = "Morelle"
    
    # Retourner le prénom sous forme de JSON
    return ({'prenom': prenom})

if _name_ == '_main_':
    # Lancer l'application Flask en mode debug
    app.run(debug=True)