# Testes API

Aqui contém testes utilizados para checar o funcionamento da API.

Será utilizada a lib `httpx` que permite requisições assíncronas.

Será usado `pytest` e os testes desenvolvidos neles serão convertido para BDD (orientado a comportamento).

Após construção do teste basta:

```pytest exemplo_2_pytest.py```

```pytest -v exemplo_2_pytest.py```

Após a utilização do **pytest** será utilizado o **behave**.

Existe uma burocracia de pastas para utilização dessa lib. Uma delas é criar o diretório `features` e organizar os arquivos dentro dele.

Após contruir os arquivos no diretório `tests/features` basta executar `behave` dentro de `tests/`.

O arquivo `tests/features/api.feature` é onde ficam escritas as regras de negócio (comportamento) que serão testadas.

BDD não é teste, desta forma a diretório `tests/features` dveria estar na raiz.

Após executar as 'features' e gerar uma pasta com 'reports':

```behave --junit```
