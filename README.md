#  Sistema de Controle de Estoque para Padaria

Este projeto é um sistema simples de controle de estoque desenvolvido em Python, voltado para o gerenciamento de produtos de uma padaria. Ele funciona via terminal e permite cadastrar, editar e acompanhar os itens disponíveis em estoque.

##  Objetivo

O objetivo deste projeto é praticar lógica de programação e conceitos fundamentais de Python, como estruturas de dados, funções e tratamento de erros, simulando um sistema real de controle de produtos.

##  Funcionalidades

*  Cadastrar produtos (nome, preço e quantidade)
*  Listar todos os produtos cadastrados
*  Buscar produto pelo nome
*  Editar informações do produto
*  Remover produtos do estoque
*  Adicionar quantidade ao estoque
*  Remover quantidade do estoque
*  Calcular o valor total do estoque
*  Alertar produtos com estoque baixo

##  Conceitos Utilizados

* Listas e dicionários
* Funções para organização do código
* Estruturas condicionais (`if/else`)
* Laços de repetição (`for`, `while`)
* Tratamento de exceções (`try/except`)
* Manipulação de strings com `.lower()` e `.strip()`

##  Como Executar

1. Certifique-se de ter o Python instalado na sua máquina
2. Baixe ou clone este repositório
3. Execute o arquivo no terminal:

```bash
python nome_do_arquivo.py
```

4. Utilize o menu interativo para navegar pelas opções

##  Estrutura dos Dados

Os produtos são armazenados em uma lista de dicionários, no seguinte formato:

```python
{
  "nome": "Pão francês",
  "preco": 0.50,
  "estoque": 100
}
```

##  Observações

* Os dados não são salvos permanentemente (não há banco de dados)
* Todas as informações são armazenadas apenas durante a execução do programa
* O sistema é totalmente baseado em terminal

##  Possíveis Melhorias

* Salvar dados em arquivo (JSON ou CSV)
* Criar interface gráfica
* Adicionar categorias de produtos
* Implementar sistema de vendas

