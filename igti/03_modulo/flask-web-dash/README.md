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
