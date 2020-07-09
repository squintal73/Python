# Consultar API viacep
# Telegram Bot: Como criar um bot, receber e enviar mensagens
# Data: 07/07/2020
# Autor: Sidnei Quintal
# V001.

import requests

token='859780563:AAGKJLs9F2sW8NvbVR3gIYXScBwxXbrt22M'

def get_msg():

    url='https://api.telegram.org/bot{0}/getUpdates'.format(token)
    r=requests.get(url)
    r_json = r.json()
   # print (r_json)
    
    for i in r_json['result']:
        nome=(i['message']['chat']['first_name'])
        ido=(i['message']['chat']['id'])
        idmsg=(i['message']['message_id'])
        texto=(i['message']['text'])
        print ("ID: " + str(ido) + " - " + str(idmsg) + " - " + nome + " - " + str(texto))
        
def send_msg():

    url='https://api.telegram.org/bot{0}/sendMessage'.format(token)
    data={'chat_id':949353603,'text':'?que tal esta?'}
    r=requests.post(url,data=data)
    print (r.content)
    

if __name__ == '__main__':
        #get_msg()
        send_msg()


