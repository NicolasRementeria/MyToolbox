import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
#import csv
import pandas as pd

class BanObject:
    def __init__(self, marca_temporal, cuando_ocurrio, plataformas, fb_user, telegram_discord_user, accion_tomada, razon, pruebas):
        self.marca_temporal = marca_temporal
        self.cuando_ocurrio = cuando_ocurrio
        self.plataformas = plataformas
        self.fb_user = fb_user
        self.telegram_discord_user = telegram_discord_user
        self.accion_tomada = accion_tomada
        self.razon = razon
        self.pruebas = pruebas

def unique_Dates(list_of_dates):
    unique_list = []
    for date in list_of_dates:
        if date not in unique_list:
            unique_list.append(date)
    return unique_list

google_creds_file = "<path_to_>\\client_secret.json"
google_spreadsheet_name = "Formulario de Blacklist (respuestas)"

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

google_spreadsheet_url_path = "https://docs.google.com/spreadsheets/d/<spreadsheet_id>/"

exported_csv_full_path = "<path_to_>\\number_of_ban_per_day.csv"

credentials = ServiceAccountCredentials.from_json_keyfile_name(google_creds_file, scope)

client = gspread.authorize(credentials)

spreadsheet = client.open_by_url(google_spreadsheet_url_path)

worksheet = spreadsheet.get_worksheet(0)

worksheet_content = worksheet.get_all_values()

ban_content = worksheet_content[1:]

ban_objects = []

for ban_item in ban_content:
    marca_temporal = datetime.strptime(ban_item[0], '%d/%m/%Y %H:%M:%S')
    #marca_temporal = ban_item[0]
    cuando_ocurrio = datetime.strptime(ban_item[1], '%d/%m/%Y')
    #cuando_ocurrio = ban_item[1]      
    plataformas = ban_item[2]
    fb_user = ban_item[3]
    telegram_discord_user = ban_item[4]
    accion_tomada = ban_item[5]
    razon = ban_item[6]
    pruebas = [ban_item[7], ban_item[8], ban_item[9]]
    ban = BanObject(marca_temporal, cuando_ocurrio, plataformas, fb_user, telegram_discord_user, accion_tomada, razon, pruebas)
    ban_objects.append(ban)

all_dates = []
for ban in ban_objects:
    all_dates.append(ban.cuando_ocurrio)

unique_dates = unique_Dates(all_dates)

unique_dates.sort()

dict_ocurrencias = {}

for unique_date in unique_dates:
    if unique_date not in dict_ocurrencias.keys():
        dict_ocurrencias[unique_date] = 0
    for ban in ban_objects:
        if unique_date == ban.cuando_ocurrio:
            dict_ocurrencias[unique_date] += 1

(pd.DataFrame.from_dict(data=dict_ocurrencias, orient='index').to_csv(exported_csv_full_path))