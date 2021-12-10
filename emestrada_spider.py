# web scraping to download pdf files

import requests
from pathlib import Path
import os
import bs4


def download_file(url, file_data):
    down_url = requests.get(url)
    subject = file_data['subject']
    year = file_data['anno']
    tema = file_data['topic'].replace('-', ' ').title()

    if tema == '':
        if file_data['convocat'] not in ['Junio', 'Septiembre']:
            convocatoria = f"{file_data['convocat'][:-1]}" \
                           f" {file_data['convocat'][-1]}"
        else:
            convocatoria = file_data['convocat']
        filename = f'{subject} - {year} - {convocatoria}'

    else:
        filename = f'{year} - {tema}'

    try:
        down_url.raise_for_status()
        url_soup = bs4.BeautifulSoup(down_url.text, 'html.parser')
        pdf_link = url_soup.select('a.pdfemb-viewer')[0].get('href')
        pdf_link_res = requests.get(pdf_link)
        with open(filename, 'wb') as pdffile:
            for chunk in pdf_link_res.iter_content(100000):
                pdffile.write(chunk)
        print(f'{filename} downloaded successfully.')
    except Exception as excp:
        not_found_error = '404 Client Error: Not Found for url:'
        if not_found_error in str(excp):
            print(f"{filename} no disponible.")
        else:
            print(f'There was an error: {excp}')


# topic names
temas_matesII = ['matrices-y-determinantes',
                 'sistemas-ecuaciones-lineales',
                 'espacio-afin-y-euclideo',
                 'funciones',
                 'integrales']
temas_sociales = ['matrices-y-determinantes',
                  'sistemas-ecuaciones-lineales',
                  'programacion-lineal',
                  'funciones',
                  'probabilidad',
                  'teoria-de-muestras',
                  'contraste-de-hipotesis']
temas_quimica = ['formulacion',
                 'la-transformacion-quimica',
                 'la-estructura-del-atomo',
                 'equilibrio-quimico',
                 'enlaces-acido-base',
                 'reacciones-redox',
                 'equilibrio-de-precipitacion',
                 'enlaces-quimicos',
                 'energia-de-las-reacciones-quimicas',
                 'quimica-organica']

temas_fisica = ['campo-gravitatorio',
                 'campo-electrico-magnetico',
                 'ondas',
                 'optica-geometrica',
                 'cuantica-nuclear']

# create folder structure
emestrada_folder = Path.home() / 'emestrada'
if not emestrada_folder.exists():
    emestrada_folder.mkdir()
os.chdir(emestrada_folder)

# (Path.cwd() / 'Mates II').mkdir()
# (Path.cwd() / 'Mates II' / 'Mates II - Temas').mkdir()
# for topic in temas_matesII:
#     folder_name = topic.replace('-', ' ').capitalize()
#     (Path.cwd() / 'Mates II' / 'Mates II - Temas' / folder_name).mkdir()
#
# (Path.cwd() / 'Mates CCSS').mkdir()
# (Path.cwd() / 'Mates CCSS' / 'Mates CCSS - Temas').mkdir()
# for topic in temas_sociales:
#     folder_name = topic.replace('-', ' ').capitalize()
#     (Path.cwd() / 'Mates CCSS' / 'Mates CCSS - Temas' / folder_name).mkdir()

# (Path.cwd() / 'Química').mkdir()
# (Path.cwd() / 'Química' / 'Química - Temas').mkdir()
# for topic in temas_quimica:
#     folder_name = topic.replace('-', ' ').capitalize()
#     (Path.cwd() / 'Química' / 'Química - Temas' / folder_name).mkdir()
if not os.path.exists(emestrada_folder / 'Fisica'):
    (emestrada_folder / 'Fisica').mkdir()
if not os.path.exists(emestrada_folder / 'Fisica' / ' Fisica - Temas'):
    (emestrada_folder / 'Fisica' / 'Fisica - Temas').mkdir()
for topic in temas_fisica:
    folder_name = topic.replace('-', ' ').capitalize()
    (emestrada_folder / 'Fisica' / 'Fisica - Temas' / folder_name).mkdir()

years = [str(i) for i in range(2000, 2022)]
convocatorias = ['junio', 'reserva1', 'reserva2', 'reserva3', 'reserva4',
                 'septiembre']

# # Mates II  ##
# # exámenes por años
#
# os.chdir(Path.cwd() / 'Mates II')
# for year in years:
#     for convocatoria in convocatorias:
#         file_data = {'subject': 'Mates II', 'anno': year,
#                      'convocat': convocatoria.capitalize(), 'topic': ''}
#         url = f'https://www.emestrada.org/{year}-{convocatoria}' \
#               f'-examen-selectividad-matematicas-andalucia/'
#
#         download_file(url, file_data)
#
# # exámenes por tema
# os.chdir(emestrada_folder / 'Mates II' / 'Mates II - Temas')
# for topic in temas_matesII:
#     folder_name = topic.replace('-', ' ').capitalize()
#     os.chdir(Path.cwd() / folder_name)
#     for year in years:
#         file_data = {'subject': 'Mates II', 'anno': year,
#                      'convocat': '', 'topic': topic}
#         url = f"https://www.emestrada.org/" \
#               f"{year}-ejercicios-resueltos-selectividad-{topic}-matematicas"
#
#         download_file(url, file_data)
#     os.chdir('..')
#
# # Mates Ciencias Sociales  ##
# # exámenes por años
# os.chdir(emestrada_folder / 'Mates CCSS')
# for year in years:
#     for convocatoria in convocatorias:
#         file_data = {'subject': 'Mates CCSS', 'anno': year,
#                      'convocat': convocatoria.capitalize(), 'topic': ''}
#         url = f"https://www.emestrada.org/{year}-" \
#               f"{convocatoria}-examen-selectividad-matematicas-ciencias" \
#               f"-sociales/"
#
#         download_file(url, file_data)
#
# # exámenes por tema
# os.chdir(emestrada_folder / 'Mates CCSS' / 'Mates CCSS - Temas')
# for topic in temas_sociales:
#     folder_name = topic.replace('-', ' ').capitalize()
#     os.chdir(Path.cwd() / folder_name)
#     for year in years:
#         file_data = {'subject': 'Mates CCSS', 'anno': year,
#                      'convocat': '', 'topic': topic}
#         url = f"https://www.emestrada.org/" \
#               f"{year}-ejercicios-resueltos-selectividad-{topic}-sociales"
#         download_file(url, file_data)
#     os.chdir('..')

# # Química ##
# # exámenes por años
# os.chdir(emestrada_folder / 'Química')
# for year in years:
#     for convocatoria in convocatorias:
#         file_data = {'subject': 'Química', 'anno': year,
#                      'convocat': convocatoria.capitalize(), 'topic': ''}
#         url = f"https://www.emestrada.org/{year}-" \
#               f"{convocatoria}-examen-selectividad-quimica-andalucia/"
#
#         download_file(url, file_data)
#
# # exámenes por tema
# os.chdir(emestrada_folder / 'Química' / 'Química - Temas')
# for topic in temas_quimica:
#     folder_name = topic.replace('-', ' ').capitalize()
#     os.chdir(Path.cwd() / folder_name)
#     for year in years:
#         file_data = {'subject': 'Química', 'anno': year,
#                      'convocat': '', 'topic': topic}
#         url = f"https://www.emestrada.org/" \
#               f"{year}-ejercicios-resueltos-selectividad-{topic}-Química"
#         # tres ultimos temas no llevan palabra Química al final de la url
#         if topic in temas_quimica[-3:]:
#             url = url[-8]
#
#         download_file(url, file_data)
#     os.chdir('..')



# # Fisica  ##
# # exámenes por años
os.chdir(emestrada_folder / 'Fisica')
for year in years:
    for convocatoria in convocatorias:
        file_data = {'subject': 'Fisica', 'anno': year,
                     'convocat': convocatoria.capitalize(), 'topic': ''}
        url = f"https://www.emestrada.org/{year}-" \
              f"{convocatoria}-examen-selectividad-fisica"

        download_file(url, file_data)

# exámenes por tema
os.chdir(emestrada_folder / 'Fisica' / 'Fisica - Temas')
for topic in temas_fisica:
    folder_name = topic.replace('-', ' ').capitalize()
    os.chdir(Path.cwd() / folder_name)
    for year in years:
        file_data = {'subject': 'Fisica', 'anno': year,
                     'convocat': '', 'topic': topic}
        url = f"https://www.emestrada.org/" \
              f"{year}-ejercicios-resueltos-selectividad-fisica-{topic}"
        download_file(url, file_data)
    os.chdir('..')
