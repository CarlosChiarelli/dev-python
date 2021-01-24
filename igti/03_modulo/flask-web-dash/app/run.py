"""Aplicativo principal."""
from flask import Flask, render_template

# adicionar o caminho para assets (= static)
app = Flask(__name__, static_folder="assets/")


@app.route('/')
def home():
    """Tela principal renderizando o template."""
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(port=5200, debug=True)
