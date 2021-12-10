from flask_app import app
import json
import jsonpickle
from flask import render_template, redirect, request, session
from ..models import owner
app.secret_key = "scdfsfds"

@app.route('/')
def index():
    owners = owner.Owner.get_all()
    print(owners)
    return render_template('index.html', owners=owners)

@app.route('/single/owner/<int:id>')
def get_one_owner(id):
    data = {
        "id": id
    }
    this_owner = owner.Owner.get_one_owner_by_id(data)
    this_ownerJSONdata = jsonpickle.encode(this_owner, indent=4)
    session['this_owner'] = this_ownerJSONdata
    return render_template('one_owner.html', this_owner=this_owner)

@app.route('/new/owner')
def new_owner():
    return render_template('create_owner.html')

@app.route('/create/owner', methods=['POST'])
def create_owner():
    owner_id = owner.Owner.create_owner(request.form)
    return redirect('/')