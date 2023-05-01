# from django.test import TestCase
# from django.contrib.auth.models import User
# from users.models import Profile

# from PIL import Image


# class ProfileModelTestCase(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.user = User.objects.create_user(username='testuser', password='testpass')
#         cls.profile = Profile.objects.create(user=cls.user.pk, bio='test bio')

#     def test_str_method(self):
#         self.assertEqual(str(self.profile), self.user.username)

#     def test_save_method(self):
#         # Test that save method resizes image when needed
#         img = Image.new('RGB', (500, 500))
#         file_path = 'test.jpg'
#         img.save(file_path)
#         self.profile.avatar = file_path
#         self.profile.save()
#         img = Image.open(self.profile.avatar.path)
#         self.assertLessEqual(img.width, 100)
#         self.assertLessEqual(img.height, 100)
