from flask import Flask, request
import socket
from datetime import date

application = Flask(__name__)


def pig_latin(word):
    word = word.lower()
    if word[0] in "aeiou":
        return word + 'yay'
    return word[1:] + word[0] + 'ay'


@application.route("/")
def countdown():
    today = date.today()
    april6 = date(2018, 4, 1)
    str_to_show = "Demo Python App \r\n Number of days to April 6:"
    
    #original_word = input('Enter something to be converted into pig latin: ')
    original_word = "Faith"
    piglatin_word = pig_latin(original_word)

    if april6 > today:
        time_to_april6 = abs(april6 - today)
        days_to_april6 = time_to_april6.days
        str_to_show += str(days_to_april6)
    # return "This is a test served from {} to {}. {}. Pig latin version of Faith is {}".format(socket.gethostname(), request.remote_addr, str_to_show, piglatin_word)
    return "{}. Pig latin version of Faith is {}".format(str_to_show, piglatin_word)

if __name__ == "__main__":
    # application.run(host='0.0.0.0')
    application.run()
