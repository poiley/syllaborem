from django.test import TestCase
from services.auth.models import User

class UserTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(display_name='chris_falken', email='littleman@gmail.com')
        self.user2 = User.objects.create(display_name='keef_m00n', email='whoareu@gmail.com')

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()

    def test_str(self):
        '''Test the __str__ function for the User model.'''
        self.assertEqual(self.user1.__str__(), 'User {username}'.format(username=self.user1.display_name))
        self.assertEqual(self.user2.__str__(), 'User {username}'.format(username=self.user2.display_name))
