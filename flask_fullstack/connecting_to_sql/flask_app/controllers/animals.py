from flask_app import app
from flask import render_template, redirect, request, session
from ..models import animal, owner

@app.route('/animals')
def animals():
    all_animals = animal.Animal.get_all_animals()
    return render_template('animal.html', all_animals=all_animals)

@app.route('/new/animal')
def new_animal():
    owners = owner.Owner.get_all()

    return render_template('create_animal.html', owners=owners)

@app.route('/create/animal', methods=['POST'])
def create_animal():
    print(request.form)
    if not animal.Animal.validate_animals(request.form):
        return redirect('/new/animal')
    new_animal_id = animal.Animal.create_animal(request.form)
    print(new_animal)

    return redirect('/animals')

@app.route('/single/animal/<int:id>')
def get_one_animal(id):
    print(id)
    owners = owner.Owner.get_all()
    data = {
        "id": id
    }
    print(data)
    this_animal = animal.Animal.get_one_animal(data)
    print(this_animal)
    return render_template('one_animal.html', this_animal=this_animal, owners=owners)

@app.route('/update/animal/<int:id>', methods=['POST'])
def get_one_and_update(id):
    print(id)
    data = {
        'id': id,
        'name': request.form['name'],
        'age': request.form['age'],
        'type': request.form['type'],
        'owner_id':request.form['owner_id']
    }
    print(data)
    animal.Animal.update_animal(data)
    return redirect('/animals')
