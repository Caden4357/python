from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from ..models import animal, owner

class Doctor:
    db_name="pet_clinic_schema"

    def __init__ (self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.animals = []

    @classmethod
    def create_doctor(cls, data):
        query = "INSERT INTO doctors (first_name, last_name) VALUES (%(first_name)s, %(last_name)s)"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        return results
