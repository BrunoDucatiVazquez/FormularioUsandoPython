from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#configurando a base de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

#schame for user 
class User(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(80), unique=True, nullable=False)
    Sobrenome = db.Column(db.String(120), unique=True, nullable=False)
    Email = db.Column(db.String(200), unique=True, nullable=False)
  
    def __repr__(self):
        return '<User %r>' % self.Nome
#route
@app.route("/home")
def homepage():
    return render_template("homepage.html")

#colocar o site no ar
if __name__ == '__main__':
    app.run(debug=True)
