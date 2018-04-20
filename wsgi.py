from flask import Flask, request
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
    therandomdate = date(2018, 6, 19)
    str_to_show = "Second version of this python App.    Number of days to June 19:"
    
    #original_word = input('Enter something to be converted into pig latin: ')
    original_word = "Mika"
    piglatin_word = pig_latin(original_word)

    if therandomdate > today:
        time_to_therandomdate = abs(therandomdate - today)
        days_to_therandomdate = time_to_therandomdate.days
        str_to_show += str(days_to_therandomdate)
    return "{}.\r\n Pig latin version of Mika is {}".format(str_to_show, piglatin_word)

if __name__ == "__main__":
    # application.run(host='0.0.0.0')
    application.run()
