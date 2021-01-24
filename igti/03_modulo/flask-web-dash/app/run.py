"""Aplicativo principal."""
from flask import Flask, render_template
from processing.processamento import Processamento

# adicionar o caminho para assets (= static)
app = Flask(__name__, static_folder="assets/")


@app.route('/')
def home():
    """Tela principal renderizando o template."""
    proc = Processamento()
    describe = proc.get_describe()
    list_temp = proc.get_list_temp()
    list_date = proc.get_list_date()
    head = proc.get_head(5)

    dados_list = [describe, list_temp, list_date, head]
    return render_template('dashboard.html', dados=dados_list)


if __name__ == '__main__':
    app.run(port=5200, debug=True)
