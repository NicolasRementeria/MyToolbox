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

exported_csv_full_path = "<path_to_>\\full_banlist_dataset.csv"

credentials = ServiceAccountCredentials.from_json_keyfile_name(google_creds_file, scope)

client = gspread.authorize(credentials)

spreadsheet = client.open_by_url(google_spreadsheet_url_path)

worksheet = spreadsheet.get_worksheet(0)

worksheet_content = worksheet.get_all_values()

pd.DataFrame.from_records(data=worksheet_content).to_csv(exported_csv_full_path)

from_list(data=worksheet_content, orient="index").to_csv(exported_csv_full_path)