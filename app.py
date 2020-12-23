from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from logica  import isMutant

app = Flask(__name__)

app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/mutante'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class esMutante(db.Model):
    __tablename__ = 'esMutante'
    id = db.Column(db.Integer, primary_key=True)
    adn = db.Column(db.String(200))

    def __init__(self, adn):
        self.adn = adn
        
class NoesMutante(db.Model):
    __tablename__ = 'NoesMutante'
    id = db.Column(db.Integer, primary_key=True)
    adn = db.Column(db.String(200))

    def __init__(self, adn):
        self.adn = adn
        

@app.route('/')
def index():
    return render_template('mutantes.html')

@app.route('/mutant/<adn>', methods=['POST'])
def post(adn):
    if request.method == "POST":
        dna= eval(adn)
        adn = dna['dna']
        if isMutant(adn):
            #if db.session.query(esMutante).filter(esMutante.adn == adn).count()== 0:
                data = esMutante(adn)
                db.session.add(data)
                db.session.commit()
                return  "Es mutante", 200
    #      else:
    #          return render_template('repetido.html')
        else:
    #      if db.session.query(NoesMutante).filter(NoesMutante.adn == dna['dna']).count()== 0:
            data = NoesMutante(dna['dna'])
            db.session.add(data)
            db.session.commit()
            return  "No es mutante", 403
            #else:
            # return render_template('repetido.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == "POST":
        adn = request.form['adn']
        print (adn)
        if isMutant(adn):
            if db.session.query(esMutante).filter(esMutante.adn == adn).count()== 0:
                data = esMutante(adn)
                db.session.add(data)
                db.session.commit()
                return render_template('agregado_m.html')
            else:
                return render_template('repetido.html')
        else:
            if db.session.query(NoesMutante).filter(NoesMutante.adn == adn).count()== 0:
                data = NoesMutante(adn)
                db.session.add(data)
                db.session.commit()
                return render_template('agregado_h.html')
            else:
                return render_template('repetido.html')

    return render_template('mutantes.html')


@app.route('/stats')
def stats():
    pass


if __name__ == "__main__":
    app.run(debug=True)