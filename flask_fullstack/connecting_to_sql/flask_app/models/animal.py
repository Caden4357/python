from flask_app.config.mysqlconnection import connectToMySQL
from ..models import owner

class Animal:
    db_name = "pet_clinic_schema"

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.age = data['age']
        self.type = data['type']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.owner = None
    @classmethod
    def get_all_animals(cls):
        query = "SELECT * FROM animals JOIN owners ON owners.id = owner_id"
        results = connectToMySQL(cls.db_name).query_db(query)
        animals = []
        for animal in results:
            this_animal = cls(animal)

            owner_info = {
                'id': animal['owners.id'],
                'first_name': animal['first_name'],
                'last_name': animal['last_name'],
                'created_at': animal['created_at'],
                'updated_at': animal['updated_at'],
            }
            this_owner = owner.Owner(owner_info)
            this_animal.owner = this_owner

            animals.append(this_animal)
        return animals

    @classmethod
    def create_animal(cls, data):
        query = "INSERT INTO animals (name, age, type, owner_id) VALUES (%(name)s, %(age)s, %(type)s, %(owner_id)s)"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        return results