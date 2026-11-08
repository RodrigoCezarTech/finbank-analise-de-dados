# Relatório Executivo — FinBank Digital

**Projeto:** Simulação corporativa de Análise de Dados e Scrum  
**Plataforma:** DataCorp Simulator  
**Natureza:** Projeto educacional  
**Data:** Novembro de 2026

## 1. Objetivo

Analisar a qualidade dos dados de transações financeiras, identificar padrões de movimentação, avaliar indicadores de risco e propor melhorias para os processos de monitoramento e tomada de decisão.

## 2. Qualidade dos dados

A base analisada apresentou:

- 391 registros originais;
- 11 registros duplicados por identificador de transação;
- 380 transações únicas após a remoção das duplicidades;
- 17 registros sem informação de cidade.

Essas inconsistências podem comprometer indicadores e relatórios gerenciais, tornando necessária a aplicação de validações antes da análise.

## 3. Indicadores financeiros

Após a remoção das duplicidades, foram identificadas:

- **340 transações aprovadas;**
- **R$ 74.828,74** em valores aprovados;
- **R$ 220,08** de ticket médio das transações aprovadas.

### Valores aprovados por categoria

| Categoria | Valor aprovado |
|---|---:|
| Compras | R$ 27.286,72 |
| Contas | R$ 21.594,01 |
| Mercado | R$ 12.575,23 |
| Alimentação | R$ 5.913,60 |
| Lazer | R$ 5.322,84 |
| Transporte | R$ 2.136,34 |

As categorias Compras e Contas representam aproximadamente **65,3%** do valor total aprovado, evidenciando concentração financeira nessas duas categorias.

### Valores aprovados por canal

| Canal | Valor aprovado |
|---|---:|
| Pix | R$ 25.010,29 |
| App | R$ 22.476,43 |
| Cartão | R$ 18.288,54 |
| Boleto | R$ 9.053,48 |

O Pix apresentou o maior valor financeiro aprovado entre os canais analisados.

## 4. Análise antifraude

Foram identificadas **16 transações classificadas como suspeitas**, equivalentes a aproximadamente **4,21%** das transações únicas.

Na política de segurança consultada durante a simulação, o limite de alerta era de **R$ 850,00**.

A análise identificou quatro transações aprovadas acima desse limite, sendo a maior de **R$ 895,16**.

A superação do limite constitui um sinal para investigação, não uma confirmação de fraude.

## 5. Dashboard de Business Intelligence

Foi construído e publicado um dashboard de barras no Studio BI, com as seguintes configurações:

- Dimensão: categoria;
- Métrica: soma dos valores;
- Filtro: somente transações aprovadas.

A visualização destacou a concentração dos valores aprovados nas categorias Compras e Contas.

## 6. Recomendações

1. Implementar validação de identificadores para reduzir registros duplicados.
2. Reforçar o preenchimento e a validação de campos obrigatórios.
3. Monitorar continuamente as transações classificadas como suspeitas.
4. Investigar as transações que ultrapassam os limites definidos na política antifraude.
5. Acompanhar indicadores financeiros por categoria e canal.
6. Utilizar dashboards gerenciais para apoiar decisões e identificar mudanças de comportamento.

## 7. Conclusão

A análise demonstrou a importância da qualidade dos dados para a confiabilidade dos indicadores financeiros.

Os resultados permitiram identificar inconsistências cadastrais, concentração de valores aprovados e ocorrências que merecem acompanhamento pelos controles antifraude.

O projeto reforçou a aplicação de Python, análise exploratória, indicadores financeiros e Business Intelligence em um cenário corporativo simulado.

---

**Nota:** Este relatório foi reconstruído após a conclusão da simulação, com base nos resultados reproduzidos no ambiente Python do DataCorp Simulator. Não representa um relatório oficial de uma instituição financeira real.