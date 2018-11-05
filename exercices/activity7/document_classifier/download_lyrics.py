# encoding=latin1

import os
import sys
import threading
import requests
from lxml.html import fromstring

def download_style(style, root):
    categorie = style.split('/')[-2]
    categorie_dir = os.path.join('corpus', categorie)
    if not os.path.exists(categorie_dir):
        os.makedirs(categorie_dir)

    print('Downloading '+categorie)

    req = requests.get(root+style)
    page = fromstring(req.content)
    urls = page.xpath('//*[@id="js-cnt-tops"]/div[3]/div[1]/ol/li/a/@href')
    total = len(urls)

    for i, url in enumerate(urls):
        print('{} of {}'.format(i, total))
        sys.stdout.write("\033[F")

        req = requests.get(root+url)
        page = fromstring(req.content)

        title = page.xpath('//*[@id="js-lyric-cnt"]/div[2]/div[2]/h1/text()')
        filename = (str(i)+'.txt').encode('latin1')


        lyrics = page.xpath(
            '//*[@id="js-lyric-cnt"]/div[3]/div[1]/article/p/text()'
        )
        try:
            lyrics = u'\n'.join(lyrics).encode('latin1')
        except:
            continue

        arq = open(os.path.join(categorie_dir, filename), 'w')
        arq.write(lyrics)
        arq.close()


root = 'https://www.letras.mus.br'
styles = [
    '/mais-acessadas/reggae/',
    '/mais-acessadas/forro/',
    '/mais-acessadas/sertanejo/',
    '/mais-acessadas/gospelreligioso/',
    '/mais-acessadas/funk/',
    '/mais-acessadas/bossa-nova/'
]

for style in styles:
    download_style(style, root)
    # thread = threading.Thread(target=download_style, args=(style, root, ))
    # thread.start()
