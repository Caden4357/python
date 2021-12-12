from flask_app import app
from flask import render_template, redirect, request, session
from ..models import animal, owner
app.secret_key = "scdfsfds"

@app.route('/animals')
def animals():
    all_animals = animal.Animal.get_all_animals()
    print(all_animals)
    return render_template('animal.html', all_animals=all_animals)

@app.route('/new/animal')
def new_animal():
    owners = owner.Owner.get_all()

    return render_template('create_animal.html', owners=owners)

@app.route('/create/animal', methods=['POST'])
def create_animal():
    print(request.form)
    new_animal_id = animal.Animal.create_animal(request.form)
    print(new_animal)

    return redirect('/animals')