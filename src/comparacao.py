import pandas as pd
import os

Cnj  = pd.read_csv("./src/data/CNJ.csv", sep=";" , encoding ="UTF-8")
Athena  = pd.read_csv("./src/data/Atena.csv", sep=";" , encoding ="UTF-8")


excesso = Cnj[~Cnj["Processo"].isin(Athena["nr_unico"])] # oque tem em um mas não no outro 

if not os.path.exists("./src/data_comparacao"):
    os.makedirs("./src/data_comparacao")

excesso.to_csv("./src/data_comparacao/excesso_processo.csv", sep= ";", encoding="UTF-8", index=False)