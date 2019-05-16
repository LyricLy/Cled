import colorama
import string


symbols = string.digits + string.ascii_letters

def color(client, message, color_scheme):
    return ({
        "BLACK": colorama.Fore.BLACK,
        "BLUE": colorama.Fore.BLUE,
        "CYAN": colorama.Fore.CYAN,
        "GREEN": colorama.Fore.GREEN,
        "MAGENTA": colorama.Fore.MAGENTA,
        "RED": colorama.Fore.RED,
        "WHITE": colorama.Fore.WHITE,
        "YELLOW": colorama.Fore.YELLOW
    }[client.config[color_scheme + "_foreground"].upper()] + {
        "BLACK": colorama.Back.BLACK,
        "BLUE": colorama.Back.BLUE,
        "CYAN": colorama.Back.CYAN,
        "GREEN": colorama.Back.GREEN,
        "MAGENTA": colorama.Back.MAGENTA,
        "RED": colorama.Back.RED,
        "WHITE": colorama.Back.WHITE,
        "YELLOW": colorama.Back.YELLOW
    }[client.config[color_scheme + "_background"].upper()]
  + message + colorama.Fore.RESET + colorama.Back.RESET)

def encode_id(x):
    digits = []
    while x:
        digits.append(symbols[int(x % 52)])
        x = int(x / 52)
    return "".join(reversed(digits))

def format_message(client, message):
    return (color(client, f"/{message.guild.name}", "server") +
            color(client, f"/{message.channel.name}", "channel") +
            color(client, f"/{encode_id(message.id)} [{message.author.name}] {message.content}", "text"))
