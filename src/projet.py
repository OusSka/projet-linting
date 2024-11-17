from flask import Flask, request, render_template

app = Flask(__name__)


# Page d'accueil pour afficher le formulaire HTML
@app.route('/')
def index():
    return render_template('index.html')  # Affiche le formulaire


# Route pour récupérer les données soumises par le formulaire
@app.route('/submit', methods=['POST'])
def submit():
    # Récupérer les données du formulaire
    name = request.form['name']
    last_name = request.form['last_name']

    # Enregistrer les données dans un fichier texte
    with open('data.txt', 'a') as f:
        f.write(f'Prenom: {name}, Nom: {last_name}\n')

    # Réponse à l'utilisateur
    return 'Données enregistrées avec succès !'


if __name__ == '__main__':
    app.run(debug=True)
