from django.test import TestCase
from apps.user.models import User as UserClass

class UserTestCase(TestCase):
    def setUp(self):
        self.user1 = UserClass.objects.create(username='chris_falken')
        self.user2 = UserClass.objects.create(username='keef_m00n')

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()

    def test_str(self):
        '''Test the __str__ function for the User model.'''
        self.assertEqual(self.user1.__str__(), 'User {username}'.format(username=self.user1.username))
        self.assertEqual(self.user2.__str__(), 'User {username}'.format(username=self.user2.username))

