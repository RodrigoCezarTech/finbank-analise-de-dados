
import csv
from collections import Counter
from pathlib import Path

ARQUIVO = Path(__file__).resolve().parent.parent / "dados" / "transacoes.csv"


def carregar_transacoes(caminho):
    with open(caminho, encoding="utf-8-sig", newline="") as arquivo:
        return list(csv.DictReader(arquivo))


def analisar_transacoes(transacoes):
    ids = set()
    registros_unicos = []
    duplicados = 0

    for transacao in transacoes:
        identificador = transacao["id_transacao"]

        if identificador in ids:
            duplicados += 1
            continue

        ids.add(identificador)
        registros_unicos.append(transacao)

    categorias = Counter(
        transacao["categoria"]
        for transacao in registros_unicos
    )

    cidades_ausentes = sum(
        not transacao.get("cidade", "").strip()
        for transacao in registros_unicos
    )

    print("=== FINBANK DIGITAL ===")
    print(f"Transações originais: {len(transacoes)}")
    print(f"Duplicidades identificadas: {duplicados}")
    print(f"Transações únicas: {len(registros_unicos)}")
    print(f"Cidades ausentes: {cidades_ausentes}")
    print("\nTransações por categoria:")

    for categoria, quantidade in categorias.most_common():
        print(f"{categoria}: {quantidade}")


if __name__ == "__main__":
    if not ARQUIVO.exists():
        print("Arquivo CSV não encontrado.")
        print("Adicione um CSV autorizado em dados/transacoes.csv.")
    else:
        analisar_transacoes(carregar_transacoes(ARQUIVO))
