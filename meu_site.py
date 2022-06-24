from flask import Flask, render_template

app = Flask(__name__)

#criar a 1º pagina do site

#route
@app.route("/")
#função
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return "Nossos contatos são:"

#colocar o site no ar
if __name__ == '__main__':
    app.run(debug=True)