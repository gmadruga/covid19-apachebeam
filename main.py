""" Pipeline de dados ApacheBeam gerador de estatisticas de covid19

Autor: Gabriel Santos Madruga Oliveira
"""
from utils import preprocessing_data_csv,preprocessing_lable_csv


def main():
    csv_rows = preprocessing_data_csv('data/HIST_PAINEL_COVIDBR_28set2020.csv',';')
    label_rows = preprocessing_lable_csv('data/EstadosIBGE.csv',';')
    print(label_rows)



if __name__ == '__main__':
    main()