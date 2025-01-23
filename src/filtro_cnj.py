import pandas as pd
import os

Cnj = pd.read_csv("src/data_cnj/Pendentes Painel CNJ - Processamento Dezembro 2024.csv", sep=";", encoding="UTF-8")

Atena = pd.read_csv("src/data_cnj/Pendentes ATENA.csv", sep=";", encoding="UTF-8")

baixados = pd.read_csv("src/data_cnj/Baixados ATENA.csv", sep=";", encoding="UTF-8")

#test
arquivo_temp = pd.read_csv("src/data_cnj/Arquivamento Temporário.csv", sep=";",
                        encoding="UTF-8",
                        dtype= {
                            'Processo': 'string',
                            'Competência': 'string',
                            'Dt Autuação': 'string',
                            'Código Classe': 'string',
                            'Classe Processual': 'string',
                            'Órgão Julgador': 'string',
                            'Dt Baixa': 'string',
                            'Local': 'string',
                            'UF': 'string',
                            'Sistema': 'string',
                            'Dt Arquiv Definitivo': 'string',
                            'Dt Suspensão': 'string',
                            'Dt Arquiv Temporário': 'string'
                        }
                        )

suspensos = pd.read_csv("src/data_cnj/Suspensos.csv", sep=";", encoding="UTF-8",
                        dtype = {
                            'Processo': 'string',
                            'Competência': 'string',
                            'Dt Autuação': 'string',
                            'Código Classe': 'string',
                            'Classe Processual': 'string',
                            'Órgão Julgador': 'string',
                            'Dt Baixa': 'string',
                            'Local': 'string',
                            'UF': 'string',
                            'Sistema': 'string',
                            'Dt Arquiv Definitivo': 'string',
                            'Dt Suspensão': 'string',
                            'Dt Arquiv Temporário': 'string'
                        }
                        )

arquivo_temp['Processo'] = arquivo_temp['Processo'].str[:7] +'-'+ arquivo_temp['Processo'].str[7:9]+'.'+arquivo_temp['Processo'].str[9:13]+ '.' +arquivo_temp['Processo'].str[13:14]+'.'+arquivo_temp['Processo'].str[14:16]+'.'+arquivo_temp['Processo'].str[16:]


suspensos['Processo'] = suspensos['Processo'].str[:7] +'-'+ suspensos['Processo'].str[7:9]+'.'+suspensos['Processo'].str[9:13]+ '.' +suspensos['Processo'].str[13:14]+'.'+suspensos['Processo'].str[14:16]+'.'+suspensos['Processo'].str[16:]

filter_Cnj = Cnj[~Cnj['Processo'].isin(Atena['nr_unico'])]


filter_Cnj_baixados = filter_Cnj[~filter_Cnj['Processo'].isin(baixados['nr_unico'])]

filter_Cnj_suspensos = filter_Cnj_baixados[~filter_Cnj_baixados['Processo'].isin(suspensos['Processo'])]

filter_arquivos_temporarios = filter_Cnj_suspensos[~filter_Cnj_suspensos['Processo'].isin(arquivo_temp['Processo'])]

os.makedirs('src/data_filter', exist_ok=True)
# filter_Cnj_baixados.to_csv("src/data_filter/filter_cnj.csv", sep=";", encoding= "UTF-8", index = False)
filter_arquivos_temporarios.to_csv("src/data_filter/filter_TEST_cnj.csv", sep=";", encoding= "UTF-8", index = False)
