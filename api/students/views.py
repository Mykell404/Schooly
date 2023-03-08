from flask_restx import Namespace, Resource, fields
from flask import request
from ..models.students import Student
from werkzeug.security import generate_password_hash
from http import HTTPStatus

student_namespace = Namespace('students', description='Student Authentication')

# Creating a new student

student_model = student_namespace.model(
    # This is a Schema (Serializer) for the student model
    'student', {
        'id': fields.Integer(required=True, description='A student id'),
        'name': fields.String(required=True, description='A student name'),
        'email': fields.String(required=True, description='A student email'),
    }
)

register_model = student_namespace.model(
    # This is a Schema (Serializer) for the signup model
    # The model comes from the namespace
    'register', {
        'name': fields.String(required=True, description='A student name'),
        'email': fields.String(required=True, description='A student email'),
        'password': fields.String(required=True, description='A student password')
    }
)

@student_namespace.route('/')
class Register(Resource):
    @student_namespace.expect(register_model)
    @student_namespace.marshal_with(student_model)
    def post(self):
        """
        Register a student
        """
        data = request.get_json()

        new_student = Student(
            name=data.get('name'),
            email=data.get('email'),
            # generate a password hash to be saved in the dbs
            password_hash=generate_password_hash(data.get('password'))
        )
        new_student.save()

        return new_student, HTTPStatus.CREATED

@student_namespace.route('/<int:id>')
class GetUpdateDelete(Resource):

    def get(self):
        """
        Reading a student
        """
        pass

    def patch(self):
        """
        Updating a student
        """
        pass

    def delete(self):
        """
        Deleting a student
        """
        pass