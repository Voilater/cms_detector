import requests
from pyfiglet import Figlet
from clint.textui import colored



banner = Figlet(font='slant')
print(colored.red(banner.renderText("WhatCMS")))

host = "github.com"

api = "https://whatcms.org/APIEndpoint/Detect"

payload = {'key': 'wh98r84gsriw3v32swoe23o1alv90tpj5b5mtf22rqr2qh6vnqe873jtgtbgj1y4kz7n09', 'url': host}

data = requests.get(api , params=payload)

json = data.json()

info = json['result']

if info['code'] == 200:
      print('Detected CMS     : %s' % info['name'])
      print('Detected Version : %s' % info['version'])
      print('Confidence       : %s' % info['confidence'])
