from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_prenom():
    # Le prénom que vous voulez retourner
    prenom = "Morelle"
    
    # Retourner le prénom sous forme de JSON
    return jsonify({'prenom': prenom})

if __name__ == '__main__':
    # Lancer l'application Flask en mode debug
    app.run(debug=True)