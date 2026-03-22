# Projeto de orçamento SINAPI
## Escopo
1 - Criar um banco de dados de composições
    - FastAPI para gerenciar requisições
    - Tipo de banco de dados: SQL
2 - Alimentar banco de dados a partir de inputs mapeados
    - pandas para leitura dos dados e padronização em um dataframe
    - definir proriedades particulares do input mapeado
    - Operação de normalizar()
3 - Ler quantitativos de projeto
    - Utilizar pandas, mas avaliar de acordo com o tipo de arquivo
    - Operação de normalizar()
4 - Definir serviços de um orçamento com base no tipo de projeto, banco de dados, quantitativo
5 - Gerar orçamento como lista de serviços
6 - Exportar orçamento em outros formatos> xlsx, pdf, html

## Operações
- [ ] Calcular expresssões matemáticas e lógicas a partir de string com o uso de funções e variáveis
- [ ] Gerar árvore de expressão e convertê-la a um formato de array
- [ ] Agrupar serviços com base em informações do quantitativo ou composição
- [ ] Ler nota de serviço* e padronizar formato de forma que possa ser facilmente acessada por meio de um identificador (ex: JSON)
- [ ] Baixar arquivos da SINAPI
- [ ] Ler arquivos da SINAPI e converter em um formato padrão das informações




* tratada aqui como forma genérica para todo quantitativo que serve como dado de entrada para o orçamento