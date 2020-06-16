from django.test import TestCase
from django.contrib.auth.models import User 

# Create your tests here.

class UserProfileTest(TestCase):

    def test_user_model_has_profile(self):
        user = User(
            email=' ejemplo@mail.com',
            username = 'user',
            password = 'abcd123',
        )

        user.save()

#va a chequear si user tiene un atributo profile
        self.assertTrue(
            hasattr(user, 'profile') 
        )