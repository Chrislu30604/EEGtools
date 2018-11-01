import requests
import os


def download_links(url, directory, name):
    r = requests.get(url)
    with open(os.path.join(directory, name), "wb") as f:
        f.write(r.content)
   
for i in range(1, 110):   
    url = f'https://physionet.org/pn4/eegmmidb/'
    dirs = f'S{i:03}'
    
    if not os.path.exists(dirs):
        os.mkdir(dirs)
    else:
        printf(f"{dir}already exists")

    for j in range(1,15):
        obj = dirs + f'R{j:02}.edf'
        parserObj = url +dirs + '/' +obj
        download_links(parserObj, dirs, obj)
