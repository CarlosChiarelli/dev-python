# language:pt

Funcionalidade: Saber qual série eu tenho
  """
  Seja uma locadora de séries
  Quero saber qual série ela tem
  """
  Cenário: No primeiro uso do sistema não devem existir séries registradas
    Quando verificar minha série em "/show/name"
    Então não devo ter nenhuma série guardada

  Cenário: Ver série registrada
    Dado que existe uma série
      | name              | episodes                                        |
      | 'Game of Thrones' | [{"name": "O casamento vermelho", "season": 2}] |
    Quando verificar minha série em "/show/name"
    Então devo ter a seguinte série armazenada
      | name              | episodes                                        |
      | 'Game of Thrones' | [{"name": "O casamento vermelho", "season": 2}] |
