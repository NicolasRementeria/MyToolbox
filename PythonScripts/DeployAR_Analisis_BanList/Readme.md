# Install gspread python library

- pip install gspread

# Install oauth2client python library

- pip install oauth2client

# Notes:

- After creating the Project & Service Account as owner or editor, check over "Service Account > Permissions" and copy your Owner/Editor member with the format {Member}@{App Name}.iam.gserviceaccount.com
- Go to your spreadsheet and give viewer/editor permissions to that particular member.

![Banfile-1](https://github.com/NicolasRementeria/PythonScripts/blob/master/DeployAR_Analisis_BanList/BanList-1.png)
![Banfile-1](https://github.com/NicolasRementeria/PythonScripts/blob/master/DeployAR_Analisis_BanList/BanList-2.png)

# Test:

```
>>> spreadsheet.title
'Formulario de Blacklist (respuestas)'

>>> worksheet.title
'Respuestas de formulario 1'

>>> worksheet.get("A1")
[['Marca temporal']]

>>> worksheet_content = worksheet.get_all_values()
>>> worksheet_content[0] 
['Marca temporal', 'Cuando ocurrió? (dia/mes/año | ej: 4/7/2020)', 'Que plataformas ', 'Si es Facebook, cual es su nombre?', 'Si es Telegram o Discod, cual es su usuario? (ej: @NicoSRE o NicoSre#1234)', 'Que acción se tomó?', 'Por que razón? (en pocas palabras)', 'Subir pruebas (imagenes)', '', '', '']


```


# Docs:

- Part of this implementation was done following:
  - https://medium.com/craftsmenltd/from-csv-to-google-sheet-using-python-ef097cb014f9

- gspread Docs>
  - https://gspread.readthedocs.io/en/latest/

# Result is located at ./number_of_ban_per_day.csv

|            | 0  |
|------------|----|
| 4/8/2020   | 1  |
| 4/10/2020  | 1  |
| 4/13/2020  | 1  |
| 4/14/2020  | 1  |
| 4/15/2020  | 1  |
| 4/20/2020  | 1  |
| 4/21/2020  | 1  |
| 4/22/2020  | 2  |
| 4/30/2020  | 2  |
| 5/4/2020   | 1  |
| 5/8/2020   | 1  |
| 5/12/2020  | 1  |
| 5/13/2020  | 1  |
| 5/14/2020  | 1  |
| 5/19/2020  | 1  |
| 5/21/2020  | 1  |
| 5/23/2020  | 1  |
| 5/25/2020  | 1  |
| 5/26/2020  | 1  |
| 5/29/2020  | 2  |
| 5/30/2020  | 2  |
| 6/1/2020   | 2  |
| 6/5/2020   | 1  |
| 6/6/2020   | 1  |
| 6/8/2020   | 3  |
| 6/10/2020  | 1  |
| 6/11/2020  | 1  |
| 6/14/2020  | 1  |
| 6/20/2020  | 1  |
| 6/21/2020  | 1  |
| 6/22/2020  | 4  |
| 6/27/2020  | 1  |
| 6/28/2020  | 1  |
| 6/29/2020  | 3  |
| 6/30/2020  | 1  |
| 7/1/2020   | 1  |
| 7/2/2020   | 2  |
| 7/8/2020   | 1  |
| 7/9/2020   | 5  |
| 7/12/2020  | 1  |
| 7/13/2020  | 1  |
| 7/15/2020  | 2  |
| 7/17/2020  | 1  |
| 7/18/2020  | 2  |
| 7/19/2020  | 1  |
| 7/20/2020  | 1  |
| 7/21/2020  | 3  |
| 7/23/2020  | 1  |
| 7/30/2020  | 2  |
| 8/2/2020   | 2  |
| 8/5/2020   | 1  |
| 8/12/2020  | 1  |
| 8/17/2020  | 1  |
| 8/18/2020  | 1  |
| 8/29/2020  | 2  |
| 8/30/2020  | 1  |
| 8/31/2020  | 1  |
| 9/2/2020   | 1  |
| 9/3/2020   | 1  |
| 9/4/2020   | 1  |
| 9/5/2020   | 1  |
| 9/7/2020   | 1  |
| 9/12/2020  | 3  |
| 9/14/2020  | 1  |
| 9/15/2020  | 1  |
| 9/18/2020  | 2  |
| 9/21/2020  | 1  |
| 9/23/2020  | 1  |
| 9/25/2020  | 1  |
| 10/1/2020  | 3  |
| 10/2/2020  | 2  |
| 10/3/2020  | 1  |
| 10/5/2020  | 1  |
| 10/6/2020  | 1  |
| 10/7/2020  | 1  |
| 10/10/2020 | 5  |
| 10/11/2020 | 1  |
| 10/12/2020 | 1  |
| 10/16/2020 | 1  |
| 10/17/2020 | 1  |
| 10/23/2020 | 3  |
| 10/24/2020 | 1  |
| 10/31/2020 | 1  |
| 11/2/2020  | 1  |
| 11/4/2020  | 2  |
| 11/5/2020  | 1  |
| 11/8/2020  | 1  |
| 11/9/2020  | 1  |
| 11/10/2020 | 22 |
| 11/11/2020 | 2  |
| 11/16/2020 | 3  |
| 11/17/2020 | 3  |
| 11/18/2020 | 2  |
| 11/23/2020 | 1  |
| 11/24/2020 | 4  |
| 11/28/2020 | 1  |
| 11/29/2020 | 1  |
| 12/1/2020  | 3  |
| 12/2/2020  | 1  |
| 12/8/2020  | 1  |
| 12/11/2020 | 1  |
| 12/12/2020 | 1  |
| 12/14/2020 | 2  |
| 12/17/2020 | 1  |
| 12/20/2020 | 3  |
| 12/22/2020 | 2  |
| 1/5/2021   | 2  |
| 1/7/2021   | 4  |
| 1/12/2021  | 1  |
| 1/14/2021  | 1  |
| 1/15/2021  | 1  |
| 1/16/2021  | 2  |
| 1/17/2021  | 1  |
| 1/18/2021  | 1  |
| 1/20/2021  | 2  |
| 1/23/2021  | 1  |
| 1/25/2021  | 1  |
| 1/26/2021  | 5  |
| 1/27/2021  | 2  |
| 1/28/2021  | 1  |
| 1/29/2021  | 1  |
| 1/30/2021  | 1  |
| 1/31/2021  | 1  |
| 2/1/2021   | 1  |
| 2/2/2021   | 3  |
| 2/5/2021   | 4  |
| 2/6/2021   | 4  |
| 2/7/2021   | 1  |
| 2/10/2021  | 1  |
| 2/21/2021  | 2  |
| 2/22/2021  | 1  |
| 2/23/2021  | 1  |
| 3/4/2021   | 1  |
| 3/7/2021   | 2  |
| 3/9/2021   | 1  |
| 3/10/2021  | 1  |
| 3/11/2021  | 1  |
| 3/12/2021  | 1  |
| 3/13/2021  | 5  |
| 4/3/2021   | 1  |
| 5/2/2021   | 1  |
