""" Arquivo com funções auxiliares utilizadas no codigo.

Autor: Gabriel Santos Madruga Oliveira
"""

import csv
import apache_beam as beam



def preprocessing_data_csv(filepath:str,delimiter:str):
    with open(filepath, mode = 'r', encoding='utf-8-sig') as csvfile:
        collection_result = []
        reader = csv.DictReader(csvfile,delimiter=delimiter)
        for row in reader:                
            collection_result.append(beam.Row(Regiao=row['regiao'],
                                            UF=row['estado'],
                                            casosNovos=int(row['casosNovos']),
                                            obitosNovos=int(row['obitosNovos']),
                                            Codigo=row['coduf']))
        return collection_result
                    

def preprocessing_lable_csv(filepath:str,delimiter:str):
    with open(filepath, mode = 'r', encoding='utf-8-sig') as csvfile:
        collection_result = []
        reader = csv.DictReader(csvfile,delimiter=delimiter)
        for row in reader:
            collection_result.append(beam.Row(Governador=row['Governador [2019]'],
                                            Estado=row['UF [-]'],
                                            Codigo=row['Código [-]']))
        return collection_result



def join_data(agg_row,label_rows):
    agg_row = agg_row._asdict()
    for label_row in label_rows:
        if agg_row['Codigo'] == label_row.Codigo:
            agg_row['Estado'] = label_row.Estado
            agg_row['Governador'] = label_row.Governador
            return beam.Row(Regiao=agg_row['Regiao'],
                            Estado=agg_row['Estado'],
                            UF=agg_row['UF'],
                            Governador=agg_row['Governador'],
                            TotalCasos=agg_row['totalCasos'],
                            TotalObitos=agg_row['totalObitos'])
        else:
            pass

    agg_row['Estado'] = ""
    agg_row['Governador'] = ""
    return beam.Row(Regiao=agg_row['Regiao'],
                        Estado=agg_row['Estado'],
                        UF=agg_row['UF'],
                        Governador=agg_row['Governador'],
                        TotalCasos=agg_row['totalCasos'],
                        TotalObitos=agg_row['totalObitos'])        


def remove_missing_values(row):
    for value in row:
        if value == "":
            return False
    return True


