```python
import unittest
from webapp.app import create_app
from webapp.models import db, User, Post

class TestModels(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_model(self):
        u = User(username='test', email='test@example.com')
        db.session.add(u)
        db.session.commit()
        self.assertTrue(User.query.filter_by(username='test').first() is not None)

    def test_post_model(self):
        u = User(username='test', email='test@example.com')
        db.session.add(u)
        p = Post(body='test post', author=u)
        db.session.add(p)
        db.session.commit()
        self.assertTrue(Post.query.filter_by(body='test post').first() is not None)

if __name__ == '__main__':
    unittest.main()
```