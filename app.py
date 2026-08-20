from flask import Flask, render_template, send_file
import qrcode
import io

app = Flask(__name__)

# Données du menu
MENU = [
    {
        "nom": "Poulet Yassa",
        "description": "Poulet mariné au citron et oignons caramélisés, servi avec du riz.",
        "prix": "4 500 FCFA",
        "categorie": "Plats",
        "image": "https://images.unsplash.com/photo-1598515214211-89d3c73ae83b?w=500"
    },
    {
        "nom": "Alloco & Poisson",
        "description": "Bananes plantains frites accompagnées de poisson grillé et sauce piquante.",
        "prix": "3 500 FCFA",
        "categorie": "Plats",
        "image": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?w=500"
    },
    {
        "nom": "Jus de Bissap",
        "description": "Boisson rafraîchissante faite maison à base de fleurs d'hibiscus et menthe.",
        "prix": "1 000 FCFA",
        "categorie": "Boissons",
        "image": "https://images.unsplash.com/photo-1544145945-f90425340c7e?w=500"
    }
]

@app.route('/')
def accueil():
    return render_template('index.html', menu=MENU)

# Route pour générer l'image du QR Code dynamiquement
@app.route('/qrcode')
def generer_qrcode():
    # Remplace l'URL ci-dessous par l'adresse finale de ton site une fois hébergé
    url_menu = "http://127.0.0.1:5000"
    
    img = qrcode.make(url_menu)
    buf = io.BytesIO()
    img.save(buf, 'PNG')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)