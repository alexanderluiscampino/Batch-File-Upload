import urllib.request, requests, os
from bs4 import BeautifulSoup

cwd = os.getcwd()
inputDir = "files/br"
inputFiles = os.listdir(os.path.join(cwd,inputDir))

# for file_ in inputFiles:
#         if file_.endswith(".txt"):
#             with open(os.path.join(inputDir,file_)) as txt_file:
#                 print(txt_file)
#                 #[print(entry.split('\n')[0]) for entry in txt_file]


payload = {'id': 'god',
            'password': 'test',
            }#'rememberMe': 'true'

with requests.Session() as s:
    url = "http://br.ims.cabal:21070/Home/LogOn?ReturnUrl=%2fGive%2fItemGive"
    p = s.post(url, data=payload)

    soup = BeautifulSoup(p.text, "html.parser")
    print(soup)
