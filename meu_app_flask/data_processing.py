import csv
import os

def read_posto_data(posto_id):
    file_path = f'./posto/{posto_id}.csv'
    if os.path.exists(file_path):
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data
    else:
        return None

def read_all_posto_data():
    posto_data = {}
    for filename in os.listdir('./posto'):
        if filename.endswith('.csv'):
            posto_id = filename.split('.')[0]
            posto_data[posto_id] = read_posto_data(posto_id)
    return posto_data
def obter_dados_do_grafico1():
    dados_posto_80 = read_posto_data('80')
    if dados_posto_80:
        datas = [row['data'] for row in dados_posto_80]
        chuvas = [row['chuva'] for row in dados_posto_80]
        return {'datas': datas, 'chuvas': chuvas}
    else:
        return None

def obter_dados_do_grafico2():
    dados_posto_133 = read_posto_data('133')
    if dados_posto_133:
        datas = [row['data'] for row in dados_posto_133]
        chuvas = [row['chuva'] for row in dados_posto_133]
        return {'datas': datas, 'chuvas': chuvas}
    else:
        return None

def obter_dados_do_grafico3():
    dados_posto_349 = read_posto_data('349')
    if dados_posto_349:
        datas = [row['data'] for row in dados_posto_349]
        chuvas = [row['chuva'] for row in dados_posto_349]
        return {'datas': datas, 'chuvas': chuvas}
    else:
        return None

