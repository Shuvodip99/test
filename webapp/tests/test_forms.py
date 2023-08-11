```python
import unittest
from flask import Flask
from webapp.forms import LoginForm, RegisterForm, PostForm
from webapp.models import User, Post

class TestForms(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config.from_object('webapp.config.TestingConfig')
        self.login_form = LoginForm()
        self.register_form = RegisterForm()
        self.post_form = PostForm()

    def test_login_form(self):
        self.login_form.username.data = 'testuser'
        self.login_form.password.data = 'testpassword'
        self.assertTrue(self.login_form.validate())

    def test_register_form(self):
        self.register_form.username.data = 'testuser'
        self.register_form.email.data = 'testuser@test.com'
        self.register_form.password.data = 'testpassword'
        self.register_form.confirm_password.data = 'testpassword'
        self.assertTrue(self.register_form.validate())

    def test_post_form(self):
        self.post_form.content.data = 'This is a test post'
        self.assertTrue(self.post_form.validate())

if __name__ == "__main__":
    unittest.main()
```