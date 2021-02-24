from django.test import TestCase
from apps.user.models import User

class UserTestCase(TestCase):
    # def setUp(self):
        

    def test_str(self):
        '''Test the __str__ function for the User model.'''
        self.user1 = User(username="chris_falken", email="cfalken@gmail.com")
        self.user2 = User(username="keef_m00n", email="whoareu@gmail.com")
        
        self.assertEqual(self.user1.__str__(), 'User {username}'.format(username=self.user1.username))
        self.assertEqual(self.user2.__str__(), 'User {username}'.format(username=self.user2.username))
