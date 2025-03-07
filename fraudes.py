import pandas as pd

# Carregar o CSV, removendo espaços extras dos nomes das colunas
fraude = pd.read_csv("./Table_fraudes.csv", sep=";", encoding="utf-8")
fraude.columns = fraude.columns.str.strip()  # Remove espaços extras nos nomes das colunas

# Converter TITULO_ELEITORAL para string
fraude["TITULO_ELEITORAL"] = fraude["TITULO_ELEITORAL"].astype(str)

# Adicionar zero à esquerda se o número tiver menos de 12 dígitos
fraude["TITULO_ELEITORAL"] = fraude["TITULO_ELEITORAL"].apply(lambda x: x.zfill(12))

# Exibir o DataFrame corrigido
fraude.to_csv("./Table_fraudes.csv", sep=";", encoding="utf-8", index=False)
