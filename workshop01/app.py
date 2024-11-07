from flask import Flask
from flask import render_template
from gen_message import WordGen

app = Flask(__name__)
possible_messages = [
"Logic will get you from A to B. Imagination will take you everywhere.",
"There are 10 kinds of people. Those who know binary and those who don't.",
"There are two ways of constructing a software design. One way is to make it \
so simple that there are obviously no deficiencies and the other is to make it \
    so complicated that there are no obvious deficiencies.",
"It's not that I'm so smart, it's just that I stay with problems longer.",
"It is pitch dark. You are likely to be eaten by a grue.",
]

@app.route('/')
def home_page():
    """
    Serves "home page" of website
    """
    generator = WordGen(possible_messages)
    message = generator.get_word()
    return render_template('index.html', someText=message)


# start 
if __name__ == "__main__":
    app.run(debug=True)