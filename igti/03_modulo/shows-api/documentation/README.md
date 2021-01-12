# Documentação e especificações

Existe uma ordem definida antes de iniciar o desenvolvimento da API propriamente dita.

* levantamento dos requisitos

* planejamento da API

* especificações usando Swagger (OpenAPI) e YAML

## Levantamento dos requisitos

Criar API que permita **incluir** e **listar séries** e **episódios dessas séries**.

1. mostrar uma série (pelo nome)

2. incluir série

3. deletar série (pelo id)

4. incluir episódio

## Planejamento da API

Perguntas que devem ser respondidas para iniciar documentação e desenvolvimento.


1. Qual é o path?

/show/{name} GET

/show POST

/show/{id} DELETE

/show/{name}/episode POST


2. Quais são os parâmetros do request?

toker JWT HEADER (json web token)
{id} ou {name} ou {name}/episode show PATH, quando necessário

3. Qual é o formato da resposta?

JSON


4. Qual é o formato do request?

JSON


5. Qual é o request body (corpo da requisição)?

/show POST -> name

/show/{name} GET ->

/show/{id} DELETE ->

/show/{name}/episode POST -> name e season


6. Qual é o response body (corpo da resposta)?

/show POST -> id, name e episodes

/show/{name} GET -> id, name e episodes

/show/{id} DELETE -> mensagem 'Excluído com sucesso'

/show/{name}/episode POST -> name e season


7. Qual é o status da resposta para operação sucesso?

200 - ok GET
201 - Criado POST
204 - Sem conteúdo DELETE


8. Qual é a resposta para operação de erro no request?

400 - Dados request enviados incorretos


9. Qual é a resposta para operação de erro de regra de negócio?

401 - Token inválido, inexistente ou expirado
404 - Recurso {id} ou {name} não encontrado


10. Qual é a resposta para operação de erro no servidor?

500 - Erro no servidor
