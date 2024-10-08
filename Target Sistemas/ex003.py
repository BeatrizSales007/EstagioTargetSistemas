# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

import json

with open('faturamento.json', 'r') as f:
    faturamento = json.load(f)

valores = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

menor_valor = min(valores)

maior_valor = max(valores)

media_mensal = sum(valores) / len(valores)

dias_acima_da_media = len([valor for valor in valores if valor > media_mensal])

print(f"Menor valor do faturamento: {menor_valor}")
print(f"Maior valor do faturamento: {maior_valor}")
print(f"Dias do faturamento acima da média: {dias_acima_da_media}")