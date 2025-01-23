import pandas as pd
import os

Cnj_execo  = pd.read_csv("./src/data_comparacao/excesso_processo.csv", sep=";" , encoding ="UTF-8")
Baixados  = pd.read_csv("./src/data/Baixado.csv", sep=";" , encoding ="UTF-8")


excesso = Cnj_execo[~Cnj_execo["Processo"].isin(Baixados["nr_unico"])] # o que tem em um mas não no outro 

if not os.path.exists("./src/data_comparacao"):
    os.makedirs("./src/data_comparacao")

excesso.to_csv("./src/data_comparacao/excesso_baixado_processo.csv", sep= ";", encoding="UTF-8", index=False)