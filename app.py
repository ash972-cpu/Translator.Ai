from flask import Flask ,render_template,request
from deep_translator import GoogleTranslator

app = Flask(__name__)

#Multi language translator
#Create Dict key value pair

languages ={
    "English": "en",
    "French":"fr",
    "Hindi":"hi",
    "German":"de",
    "Arabic":"ar",
    "Korean":"ko",
}
#Create a home route (/) and route accept botn GET AND POST method
@app.route("/",methods=["GET","POST"])
def index():
    translated =""
    if request.method =="POST":
        text = request.form["text"]
        source = request.form["source"]
        target = request.form["target"]

        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

    return render_template("index.html",
                           languages = languages,
                           translated = translated)
if __name__ == "__main__":
    app.run(debug=True)

