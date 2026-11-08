
"""
FinBank Digital — Análise de Transações Financeiras

Projeto educacional desenvolvido a partir de uma simulação
corporativa no DataCorp Simulator.

Execução:
    python notebooks/analise_finbank.py

O CSV deve estar em dados/transacoes.csv.
Não publique dados internos sem autorização.
"""

import csv
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
ARQUIVO = BASE / "dados" / "transacoes.csv"

LIMITE_ALERTA = 850.00


def carregar_dados(caminho):
    with open(caminho, "r", encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=";")

        if leitor.fieldnames and len(leitor.fieldnames) == 1:
            arquivo.seek(0)
            leitor = csv.DictReader(arquivo, delimiter=",")

        campos = {"id_transacao", "valor", "status", "categoria", "cidade"}
        faltantes = campos - set(leitor.fieldnames or [])

        if faltantes:
            raise ValueError(
                f"Colunas obrigatórias ausentes: {sorted(faltantes)}"
            )

        return list(leitor)


def converter_valor(texto):
    texto = str(texto or "0").strip()

    if "," in texto:
        texto = texto.replace(".", "").replace(",", ".")

    return float(texto)


def formatar_reais(numero):
    return (
        f"R$ {numero:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


def analisar(dados):
    ids = set()
    unicas = []
    duplicadas = 0

    for transacao in dados:
        identificador = str(transacao["id_transacao"]).strip()

        if identificador in ids:
            duplicadas += 1
            continue

        ids.add(identificador)
        unicas.append(transacao)

    sem_cidade = sum(
        not str(t.get("cidade") or "").strip()
        for t in unicas
    )

    aprovadas = [
        t for t in unicas
        if str(t["status"]).strip().lower() in ("aprovada", "aprovado")
    ]

    suspeitas = [
        t for t in unicas
        if str(t["status"]).strip().lower() in ("suspeita", "suspeito")
    ]

    total_aprovado = sum(
        converter_valor(t["valor"]) for t in aprovadas
    )

    ticket_medio = (
        total_aprovado / len(aprovadas)
        if aprovadas else 0
    )

    por_categoria = defaultdict(float)
    por_canal = defaultdict(float)

    for t in aprovadas:
        valor = converter_valor(t["valor"])
        por_categoria[t["categoria"]] += valor
        por_canal[t.get("canal") or "Não informado"] += valor

    acima_limite = [
        t for t in aprovadas
        if converter_valor(t["valor"]) > LIMITE_ALERTA
    ]

    maior_valor = max(
        (converter_valor(t["valor"]) for t in aprovadas),
        default=0
    )

    print("=" * 55)
    print("FINBANK DIGITAL — RELATÓRIO DE ANÁLISE")
    print("=" * 55)

    print("\n1. QUALIDADE DOS DADOS")
    print("Registros originais:", len(dados))
    print("Duplicidades:", duplicadas)
    print("Transações únicas:", len(unicas))
    print("Registros sem cidade:", sem_cidade)

    print("\n2. INDICADORES FINANCEIROS")
    print("Transações aprovadas:", len(aprovadas))
    print("Transações suspeitas:", len(suspeitas))
    print("Total aprovado:", formatar_reais(total_aprovado))
    print("Ticket médio:", formatar_reais(ticket_medio))

    print("\n3. VALORES APROVADOS POR CATEGORIA")
    for categoria, total in sorted(
        por_categoria.items(), key=lambda x: x[1], reverse=True
    ):
        print(f"{categoria}: {formatar_reais(total)}")

    print("\n4. VALORES APROVADOS POR CANAL")
    for canal, total in sorted(
        por_canal.items(), key=lambda x: x[1], reverse=True
    ):
        print(f"{canal}: {formatar_reais(total)}")

    print("\n5. ANÁLISE ANTIFRAUDE")
    print("Limite de alerta:", formatar_reais(LIMITE_ALERTA))
    print("Aprovadas acima do limite:", len(acima_limite))
    print("Maior transação aprovada:", formatar_reais(maior_valor))

    print("\nAnálise concluída.")


if __name__ == "__main__":
    if not ARQUIVO.exists():
        print("CSV não encontrado:", ARQUIVO)
        print("Adicione um CSV autorizado na pasta dados/.")
    else:
        try:
            analisar(carregar_dados(ARQUIVO))
        except (ValueError, KeyError, OSError) as erro:
            print("Erro ao analisar os dados:", erro)
