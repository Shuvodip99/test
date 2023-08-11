```python
import unittest
from flask import url_for
from webapp import app, db
from webapp.models import User, Post

class TestViews(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_home_page(self):
        response = self.app.get(url_for('home'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.app.get(url_for('login'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        response = self.app.get(url_for('register'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_valid_user_registration(self):
        response = self.app.post(
            '/register',
            data=dict(username='test', email='test@test.com', password='test123', confirm='test123'),
            follow_redirects=True
        )
        self.assertIn(b'Registration successful', response.data)
        user = User.query.filter_by(email='test@test.com').first()
        self.assertTrue(user)

    def test_valid_user_login(self):
        user = User(username='test', email='test@test.com', password='test123')
        db.session.add(user)
        db.session.commit()
        response = self.app.post(
            '/login',
            data=dict(email='test@test.com', password='test123'),
            follow_redirects=True
        )
        self.assertIn(b'Login successful', response.data)

    def test_valid_post_creation(self):
        user = User(username='test', email='test@test.com', password='test123')
        db.session.add(user)
        db.session.commit()
        response = self.app.post(
            '/post',
            data=dict(title='Test Post', content='This is a test post', author=user),
            follow_redirects=True
        )
        self.assertIn(b'Post created', response.data)
        post = Post.query.filter_by(title='Test Post').first()
        self.assertTrue(post)

if __name__ == "__main__":
    unittest.main()
```