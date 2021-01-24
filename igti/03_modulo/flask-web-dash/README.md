## Flask para web (front-end)

A partir daqui será construído um front-end (dashboards) usando templates prontos junto Flask renderizando páginas web.

No site abaixo do [Create Tim](https://www.creative-tim.com/) é possível encontrar diversos templates.

Para utilizar os gráficos responsivos será utilizado o [Chartisti.js](http://gionkunz.github.io/chartist-js/).

Passos:

* download do [template](creative-tim.com/product/material-dashboard)

* extrair e clicar pasta `app/`

* separar pastas `assets` e `examples` (renomeada para 'templates') para `app/`

* criar arquivo de execução da aplicação `aap/run.py`

* dizer ao Flask quais templates (`examples`) utilizar em cada rota

* criar pasta `app/data` com dados de temperatura

* alterar os elementos web (`templates/dashboards.html`) inspecionando no browser e buscando/editando

* gerar processamento dos dados em `app/processing`

* adicionar processamento em `app/run.py`

* alterar `templates/dashboard.html` para inserir os dados dinâmicos processados

* alterar os ícones da primeira linha utilizando [bootstrap icons](https://icons.getbootstrap.com/) alterando-os em `templates/dashboard.html` com o nome que aparece na página. Nesse caso será usado os ícones indicado em `templates/icons.html`

* alterando o próprio gráfico em `templates/dashboard.html`

* é posssível ver o **gráfico dinâmico** web contido em `app/assets/js/material-dashboards.js` que são **organizados** em **labels** (axis-x) e **séries** (valor em sí)

* criar métods em `run.py` para enviar dados do gráfico e alterar para os dados recebidos em `templates/dashboard.html`

* alterar tabela `templates/dashboard.html` e enviar as dados pelo back-end `processing/processamento.py`
