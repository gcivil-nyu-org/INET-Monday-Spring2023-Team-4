from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core import mail
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.core.files.uploadedfile import SimpleUploadedFile

from PIL import Image
from io import BytesIO

from users.models import Profile
from users.forms import UpdateUserForm, UpdateProfileForm, RegisterForm


class TestRegisterView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("users-register")
        self.valid_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password1": "testpassword123",
            "password2": "testpassword123",
        }
        self.invalid_data = {
            "username": "",
            "email": "invalid_email",
            "password1": "short",
            "password2": "longer",
        }

    def test_register_view_get(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/register.html")
        self.assertIsInstance(response.context["form"], RegisterForm)

    # def test_register_view_post_valid_data(self):
    #     response = self.client.post(self.url, self.valid_data)

    #     self.assertRedirects(response, reverse("login"))
    #     self.assertEqual(User.objects.count(), 1)
    #     self.assertEqual(User.objects.first().username, self.valid_data["username"])

    def test_register_view_post_invalid_data(self):
        response = self.client.post(self.url, self.invalid_data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/register.html")
        self.assertIn("form", response.context)
        self.assertTrue(response.context["form"].has_error("username"))
        self.assertTrue(response.context["form"].has_error("email"))
        self.assertEqual(User.objects.count(), 0)

    def test_register_view_post_authenticated_user(self):
        self.client.force_login(User.objects.create_user(username="test"))

        response = self.client.get(self.url)
        self.assertRedirects(response, "/")

        response = self.client.post(self.url, self.valid_data)
        self.assertRedirects(response, "/")
        self.assertEqual(User.objects.count(), 1)


class TestCustomLoginView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("login")
        self.credentials = {"username": "testuser", "password": "testpassword123"}
        self.user = User.objects.create_user(**self.credentials)

    def test_custom_login_view_get(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, "registration/login.html")
        self.assertIsInstance(response.context["form"], AuthenticationForm)
        # self.assertNotIn("remember_me", response.context["form"].fields)

    def test_custom_login_view_post_remember_me(self):
        response = self.client.post(self.url, {**self.credentials, "remember_me": True})

        self.assertRedirects(response, "/")
        self.assertIn("_auth_user_id", self.client.session)

    def test_custom_login_view_post_not_remember_me(self):
        response = self.client.post(
            self.url, {**self.credentials, "remember_me": False}
        )

        self.assertRedirects(response, "/")
        self.assertIn("_auth_user_id", self.client.session)

    def test_custom_login_view_post_invalid_credentials(self):
        response = self.client.post(
            self.url, {"username": "invalid", "password": "invalid"}
        )

        self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, "registration/login.html")
        # self.assertIn("form", response.context)
        # self.assertTrue(response.context["form"].has_error("username"))
        # self.assertTrue(response.context["form"].has_error("password"))

    def test_custom_login_view_post_already_authenticated(self):
        self.client.force_login(self.user)

        response = self.client.get(self.url)
        self.assertRedirects(response, "/")

        response = self.client.post(self.url, self.credentials)
        self.assertRedirects(response, "/")


class ResetPasswordViewTest(TestCase):
    def test_reset_password_page_status_code(self):
        response = self.client.get(reverse("password_reset"))
        self.assertEqual(response.status_code, 200)

    # def test_reset_password_submit_valid_email(self):
    #     response = self.client.post(
    #         reverse("password_reset"),
    #         data={"email": "test@example.com"},
    #     )
    #     self.assertRedirects(response, reverse("password_reset_complete"))

    def test_reset_password_submit_invalid_email(self):
        response = self.client.post(
            reverse("password_reset"),
            data={"email": "invalidemail"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enter a valid email address.")

    # def test_reset_password_success_message(self):
    #     response = self.client.post(
    #         reverse("password_reset"),
    #         data={"email": "test@example.com"},
    #     )
    #     self.assertContains(
    #         response,
    #         "We've emailed you instructions for setting your password",
    #         count=1,
    #         status_code=302,
    #     )

    def test_reset_password_success_url(self):
        response = self.client.post(
            reverse("password_reset"),
            data={"email": "test@example.com"},
            follow=True,
        )
        self.assertRedirects(response, reverse("users-home"))


class ChangePasswordViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpass123",
        )
        self.url = reverse_lazy("password_change")
        self.client.login(username="testuser", password="testpass123")

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, "Change Password")
        # self.assertContains(response, "Old password")
        # self.assertContains(response, "New password")
        # self.assertContains(response, "Confirm new password")

    def test_post_success(self):
        data = {
            "old_password": "testpass123",
            "new_password1": "newtestpass123",
            "new_password2": "newtestpass123",
        }
        response = self.client.post(self.url, data=data)
        self.assertRedirects(response, reverse_lazy("users-home"))
        self.assertEqual(len(mail.outbox), 0)
        # self.assertContains(response, "Successfully Changed Your Password")

    def test_post_failure(self):
        data = {
            "old_password": "wrongpassword",
            "new_password1": "newtestpass123",
            "new_password2": "newtestpass123",
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your old password was entered incorrectly.")


# class ProfileViewTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create_user(
#             username="testuser", password="testpass123"
#         )
#         self.profile = Profile.objects.create(user=self.user)

#     def test_view_with_unauthenticated_user(self):
#         self.client.logout()
#         response = self.client.get(reverse("users-profile"))
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, "/login/?next=/profile/")

#     def test_view_with_authenticated_user(self):
#         self.client.login(username="testuser", password="testpass123")
#         response = self.client.get(reverse("users-profile"))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, "users/profile.html")
