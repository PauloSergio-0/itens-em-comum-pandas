import pandas as pd
import os

alunos_antigos  = pd.read_csv("./src/data/alunos_csv1.csv", sep="," , encoding ="UTF-8")
alunos_atual  = pd.read_csv("./src/data/alunos_csv2.csv", sep="," , encoding ="UTF-8")


alunos_n_presente = alunos_antigos[~alunos_antigos["codigo_aluno"].isin(alunos_atual["codigo_aluno"])] # oque tem em um mas não no outro 

if not os.path.exists("./src/result_data"):
    os.makedirs("./src/result_data")

alunos_n_presente.to_csv("./src/result_data/alunos_N_presentes.csv", sep= ";", encoding="UTF-8")