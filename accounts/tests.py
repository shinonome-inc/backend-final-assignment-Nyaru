# from django.test import TestCase
from django.contrib.auth import SESSION_KEY, get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class TestSignupView(TestCase):
    def setUp(self):
        self.url = reverse("accounts:signup")

    # get test
    def test_success_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/signup.html")

    # post test
    def test_success_post(self):
        valid_data = {
            "username": "testuser",
            "email": "test@test.com",
            "password1": "testpassword",
            "password2": "testpassword",
        }
        response = self.client.post(self.url, valid_data)
        # 1の確認 = tweets/homeにリダイレクトすること
        self.assertRedirects(
            response,
            reverse("tweets:home"),
            status_code=302,
            target_status_code=200,
        )
        # 2の確認 = ユーザーが作成されること
        self.assertTrue(User.objects.filter(username=valid_data["username"]).exists())
        # 3の確認 = ログイン状態になること
        self.assertIn(SESSION_KEY, self.client.session)

    # 異常系test
    # form empty test
    def test_failure_post_with_empty_form(self):
        invalid_data = {
            "username": "",
            "email": "",
            "password1": "",
            "password2": "",
        }
        response = self.client.post(self.url, invalid_data)
        form = response.context["form"]
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username=invalid_data["username"]).exists())
        self.assertFalse(form.is_valid())
        self.assertIn("このフィールドは必須です。", form.errors["username"])
        self.assertIn("このフィールドは必須です。", form.errors["email"])
        self.assertIn("このフィールドは必須です。", form.errors["password1"])
        self.assertIn("このフィールドは必須です。", form.errors["password2"])

    # username empty test
    def test_failure_post_with_empty_username(self):
        print(self.url)
        invalid_data = {
            "username": "",
            "email": "test@test.com",
            "password1": "testpassword",
            "password2": "testpassword",
        }
        response = self.client.post(self.url, invalid_data)
        print(response.context)
        form = response.context["form"]
        print(form.errors)

        # don't redirect
        self.assertEqual(response.status_code, 200)
        # exist error
        self.assertFalse(User.objects.filter(username=invalid_data["username"]).exists())
        # よくわからん
        self.assertFalse(form.is_valid())
        # Error message
        self.assertIn("このフィールドは必須です。", form.errors["username"])

    # email empty test
    def test_failure_post_with_empty_email(self):
        invalid_data = {
            "username": "testuser",
            "email": "",
            "password1": "testpassword",
            "password2": "testpassword",
        }
        response = self.client.post(self.url, invalid_data)
        form = response.context["form"]

        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username=invalid_data["username"]).exists())
        self.assertFalse(form.is_valid())
        self.assertIn("このフィールドは必須です。", form.errors["email"])

    #   password empty test
    def test_failure_post_with_empty_password(self):
        invalid_data = {
            "username": "testuser",
            "email": "test@test.com",
            "password1": "",
            "password2": "",
        }
        response = self.client.post(self.url, invalid_data)
        form = response.context["form"]

        self.assertEqual(response.status_code, 200)
        # exist error
        self.assertFalse(User.objects.filter(username=invalid_data["username"]).exists())
        # よくわからん
        self.assertFalse(form.is_valid())
        # Error message
        self.assertIn("このフィールドは必須です。", form.errors["password1"])
        self.assertIn("このフィールドは必須です。", form.errors["password2"])


# class TestSignupView(TestCase):
#     def test_success_get(self):

#     def test_success_post(self):

#     def test_failure_post_with_empty_form(self):

#     def test_failure_post_with_empty_username(self):

#     def test_failure_post_with_empty_email(self):

#     def test_failure_post_with_empty_password(self):

#     def test_failure_post_with_duplicated_user(self):

#     def test_failure_post_with_invalid_email(self):

#     def test_failure_post_with_too_short_password(self):

#     def test_failure_post_with_password_similar_to_username(self):

#     def test_failure_post_with_only_numbers_password(self):

#     def test_failure_post_with_mismatch_password(self):


# class TestLoginView(TestCase):
#     def test_success_get(self):

#     def test_success_post(self):

#     def test_failure_post_with_not_exists_user(self):

#     def test_failure_post_with_empty_password(self):


# class TestLogoutView(TestCase):
#     def test_success_post(self):


# class TestUserProfileView(TestCase):
#     def test_success_get(self):


# class TestUserProfileEditView(TestCase):
#     def test_success_get(self):

#     def test_success_post(self):

#     def test_failure_post_with_not_exists_user(self):

#     def test_failure_post_with_incorrect_user(self):


# class TestFollowView(TestCase):
#     def test_success_post(self):

#     def test_failure_post_with_not_exist_user(self):

#     def test_failure_post_with_self(self):


# class TestUnfollowView(TestCase):
#     def test_success_post(self):

#     def test_failure_post_with_not_exist_tweet(self):

#     def test_failure_post_with_incorrect_user(self):


# class TestFollowingListView(TestCase):
#     def test_success_get(self):


# class TestFollowerListView(TestCase):
#     def test_success_get(self):
