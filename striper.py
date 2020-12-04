import re

def striper(string):
    str_data = ""
    try :
        data = re.search(
            ':(.*)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)', string
        ).groups()

        str_data = f"{data[2]}"
    except Exception:
        pass

    return str_data

if __name__ == "__main__":
    striper("")