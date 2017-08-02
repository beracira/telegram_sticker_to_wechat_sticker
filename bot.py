#! /usr/bin/python3

import time
import pprint
import telepot
from PIL.Image import open as open_image
from telepot.loop import MessageLoop

print = pprint.PrettyPrinter().pprint

def handle(msg):
    print (msg)
    content_type, chat_type, chat_id = telepot.glance(msg)

    print ('Content type: %s' % content_type)

    if content_type == 'sticker':
        print ('start downloading...')
        bot.download_file(msg['sticker']['file_id'], './fin.webp')

        print ('download finished. start converting...')
        # only gif can be added to wechat sticker pack. 
        # and it only checks extension of the file but not the actual format
        open_image('fin.webp').save('fout.gif', 'PNG')
        print ('conversion done.')
        
        fout = open('fout.gif', 'rb')
        print ('sending photo...')
        bot.sendDocument(chat_id, fout)
    else:
        bot.sendMessage(chat_id, 'I will only accept stickers for now.')

bot = telepot.Bot('***Your Token Here***')

MessageLoop(bot, handle).run_as_thread()
print ('I am listening ...')

while 1:
    time.sleep(10)
