"""
BaseTest

Esta clase deberia ser la clase padre para cada test no unitario.
Permite la instanciacion de una Data Base dinamicamente y asegurandose de que 
sea nueva y este en blanco cada vez que se ejecuten los test.

"""

from unittest import TestCase
from app import app
from db import db


class  BaseTest(TestCase):
    def setUp(self):
        #make sure database exist
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()
        #get a test client 
        self.app = app.test_client()
        self.app_context = app.app_context

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()