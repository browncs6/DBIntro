#!/usr/bin/env python3

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


# full form: postgresql://username:password@hostname/database
postgres_master = 'postgresql://localhost/cs6'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = postgres_master
app.config['DEBUG'] = True
db = SQLAlchemy(app)


# define Pokemon
class Pokemon(db.Model):
    __tablename__ = 'pokemon'

    name = db.Column(db.String(64), primary_key=True)
    category = db.Column(db.String(64))
    height_ft = db.Column(db.Numeric())
    weight_lbs = db.Column(db.Numeric())

    def height(self):
        """ returns height in m """
        return float(self.height_ft) * .3048

    def weight(self):
        """ returns weight in kg """
        return float(self.weight_lbs) * .453592

@app.route('/', methods=['GET', 'POST'])
def index():

    # check if post request
    # if so, add new pokemon!
    if request.method == 'POST':
        poke = Pokemon(name=request.form['name'],
                       category=request.form['category'],
                       height_ft=request.form['height_ft'],
                       weight_lbs=request.form['weight_lbs'])

        db.session.add(poke)   # add to database (transaction)
        db.session.commit()    # commit transaction


    pokemon = Pokemon.query.all()
    return render_template('index.html', pokemon = pokemon)

@app.route('/pokemon/<name>')
def show_pokemon(name):
    pokemon = Pokemon.query.filter_by(name=name).first_or_404()

    return render_template('show_pokemon.html', pokemon=pokemon)


if __name__ == '__main__':

    # use FLASK shell, i.e.
    # export FLASK_APP=02_app.py
    # flask shell
    # from poke import db
    # db.create_all()

    # ==> use db.drop_all() to remove model
    # ==> use db.crete_all() to create schema

    app.run()
