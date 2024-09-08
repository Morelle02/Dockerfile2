from flask import Flask, jsonify

# Créer une instance de l'application Flask
app = Flask(__name__)

@app.route('/')
def get_prenom():
    # Le prénom que vous voulez retourner
    prenom = "Morelle"
    
    # Retourner le prénom sous forme de JSON
    return jsonify({'prenom': prenom})

# Vérifier si le script est exécuté directement
if __name__ == '__main__':
    # Lancer l'application Flask en mode debug
    app.run(debug=True , host="0.0.0.0", port=5000)