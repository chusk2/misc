# Web scrapping of PDF files from:
# https://www.perfect-english-grammar.com/english-language-pdf.html

import requests
from pathlib import Path
import os
from bs4 import BeautifulSoup


def download_file(url):
    down_url = requests.get(url)
    try:
        down_url.raise_for_status()
        url_soup = BeautifulSoup(down_url.text, 'html.parser')
        links = url_soup.find_all('a')
        pdf_links = []
        for link in links:
            # not all links have href attribute
            try:
                if link['href'].endswith('.pdf'):
                    pdf_links.append(link['href'])
            except KeyError:
                continue
        for pdf in pdf_links:
            pdf_link_res = requests.get(pdf)
            # get the pdf filename
            # find the last forward slash position in string.
            # From here, there's the pdf filename
            index_counting_backwards = pdf[::-1].find('/')
            filename = pdf[len(pdf)-index_counting_backwards:]
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


# create folder structure
pdf_folder = Path.home() / 'Grammar PDFs'
if not pdf_folder.exists():
    pdf_folder.mkdir()
os.chdir(pdf_folder)

os.chdir(pdf_folder)
url = "https://www.perfect-english-grammar.com/english-language-pdf.html"
download_file(url)
