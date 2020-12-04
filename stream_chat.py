import socket
import logging
from striper import striper
from emoji import demojize

import os
from dotenv import load_dotenv

load_dotenv()


logging.basicConfig(level=logging.DEBUG,
                    format='%(message)s',
                    handlers=[logging.FileHandler('chat.log', encoding='utf-8')])


server = 'irc.chat.twitch.tv'
port = 6667
nickname = os.getenv('NICKNAME')
token = os.getenv('TOKEN')
channel = os.getenv('CHANNEL')

def chat()->None:
    s = socket.socket()

    s.connect((server, port))

    s.send(f"PASS {token}\n".encode('utf-8'))
    s.send(f"NICK {nickname}\n".encode('utf-8'))
    s.send(f"JOIN {channel}\r\n".encode('utf-8'))
    try :
        while True:
            resp = s.recv(2048).decode('utf-8')
            if resp.startswith('PING'):
                s.send("PONG\n".encode('utf-8'))

            elif len(resp) > 0:
                str_resp = striper(resp)
                print(f"{str_resp}")
                logging.info(demojize(str_resp))

    except KeyboardInterrupt:
        s.close()
        exit()

if __name__ == "__main__":
    chat()