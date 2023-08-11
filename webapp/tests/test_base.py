import unittest
from flask import current_app
from webapp.app import create_app
from webapp.config import TestConfig
from webapp.models import db, User, Post

class TestBase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_user_model(self):
        u = User(username='test', email='test@example.com')
        db.session.add(u)
        db.session.commit()
        self.assertEqual(User.query.get(1).username, 'test')

    def test_post_model(self):
        u = User(username='test', email='test@example.com')
        db.session.add(u)
        p = Post(body='test post', author=u)
        db.session.add(p)
        db.session.commit()
        self.assertEqual(Post.query.get(1).body, 'test post')