# from django.contrib.auth import SESSION_KEY, get_user_model
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from tweets.models import Tweet

User = get_user_model()
Model = Tweet


# class TestSignupView(TestCase):
#     def setUp(self):
#         self.url = reverse("accounts:signup")
#         self.user = User.objects.create_user(username="tester", password="testpassword")

#     # Test Case 1-1
#     def test_success_get(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, "accounts/signup.html")

#     # Test Case 1-2,2-1
#     def test_success_post(self):
#         valid_data = {
#             "username": "testuser",
#             "email": "test@test.com",
#             "password1": "testpassword",
#             "password2": "testpassword",
#         }
#         response = self.client.post(self.url, valid_data)
#         print(response)
#         self.assertRedirects(
#             response,
#             # reverse("tweets:home"), # 1-2
#             reverse(settings.LOGIN_REDIRECT_URL),  # 2-1
#             status_code=302,
#             target_status_code=200,
#         )
#         self.assertTrue(User.objects.filter(username=valid_data["username"]).exists())
#         self.assertIn(SESSION_KEY, self.client.session)

#     # 異常系test
#     # Test Case 1-3
#     def test_failure_post_with_empty_form(self):
#         invalid_data = {
#             "username": "",
#             "email": "",
#             "password1": "",
#             "password2": "",
#         }
#         response = self.client.post(self.url, invalid_data)
#         form = response.context["form"]

#         self.assertEqual(response.status_code, 200)
#         self.assertFalse(User.objects.filter(username=invalid_data["username"]).exists())
#         self.assertFalse(form.is_valid())
#         self.assertIn("このフィールドは必須です。", form.errors["username"])
#         self.assertIn("このフィールドは必須です。", form.errors["email"])
#         self.assertIn("このフィールドは必須です。", form.errors["password1"])
#         self.assertIn("このフィールドは必須です。", form.errors["password2"])

#     # Test Case 1-4
#     def test_failure_post_with_empty_username(self):
#         print(self.url)
#         invalid_data = {
#             "username": "",
#             "email": "test@test.com",
#             "password1": "testpassword",
#             "password2": "testpassword",
#         }
#         response = self.client.post(self.url, invalid_data)
#         form = response.context["form"]

#         self.assertEqual(response.status_code, 200)
#         self.assertFalse(User.objects.filter(username=invalid_data["username"]).exists())
#         self.assertFalse(form.is_valid())
#         self.assertIn("このフィールドは必須です。", form.errors["username"])

#     # Test Case 1-5
#     def test_failure_post_with_empty_email(self):
#         invalid_data = {
#             "username": "testuser",
#             "email": "",
#             "password1": "testpassword",
#             "password2": "testpassword",
#         }
#         response = self.client.post(self.url, invalid_data)
#         form = response.context["form"]

#         self.assertEqual(response.status_code, 200)
#         self.assertFalse(User.objects.filter(username=invalid_data["username"]).exists())
#         self.assertFalse(form.is_valid())
#         self.assertIn("このフィールドは必須です。", form.errors["email"])

#     # Test Case 1-6
#     def test_failure_post_with_empty_password(self):
#         invalid_data = {
#             "username": "testuser",
#             "email": "test@test.com",
#             "password1": "",
#             "password2": "",
#         }
#         response = self.client.post(self.url, invalid_data)
#         form = response.context["form"]

#         self.assertEqual(response.status_code, 200)
#         # exist error
#         self.assertFalse(User.objects.filter(username=invalid_data["username"]).exists())
#         # よくわからん
#         self.assertFalse(form.is_valid())
#         # Error message
#         self.assertIn("このフィールドは必須です。", form.errors["password1"])
#         self.assertIn("このフィールドは必須です。", form.errors["password2"])

#     # Test Case 1-7
#     def test_failure_post_with_duplicated_user(self):
#         invalid_data = {
#             "username": "tester",
#             "email": "test@test.com",
#             "password1": "testpassword",
#             "password2": "testpassword",
#         }
#         response = self.client.post(self.url, invalid_data)
#         form = response.context["form"]

#         self.assertEqual(response.status_code, 200)
#         self.assertTrue(User.objects.filter(username=invalid_data["username"]).exists())
#         self.assertFalse(form.is_valid())
#         self.assertIn("同じユーザー名が既に登録済みです。", form.errors["username"])

#     # Test Case 1-8
#     def test_failure_post_with_invalid_email(self):
#         invalid_data = {
#             "username": "testuser",
#             "email": "test",
#             "password1": "testpassword",
#             "password2": "testpassword",
#         }
#         response = self.client.post(self.url, invalid_data)
#         form = response.context["form"]

#         self.assertEqual(response.status_code, 200)
#         self.assertFalse(User.objects.filter(username=invalid_data["username"]).exists())
#         self.assertFalse(form.is_valid())
#         self.assertIn("有効なメールアドレスを入力してください。", form.errors["email"])

#     # Test Case 1-9
#     def test_failure_post_with_too_short_password(self):
#         invalid_data = {
#             "username": "testuser",
#             "email": "test@test.com",
#             "password1": "aaa",
#             "password2": "aaa",
#         }
#         response = self.client.post(self.url, invalid_data)
#         form = response.context["form"]

#         self.assertEqual(response.status_code, 200)
#         self.assertFalse(User.objects.filter(username=invalid_data["username"]).exists())
#         self.assertFalse(form.is_valid())
#         self.assertIn("このパスワードは短すぎます。最低 8 文字以上必要です。", form.errors["password2"])

#     # Test Case 1-10
#     def test_failure_post_with_password_similar_to_username(self):
#         invalid_data = {
#             "username": "testuser",
#             "email": "test@test.com",
#             "password1": "testuser",
#             "password2": "testuser",
#         }
#         response = self.client.post(self.url, invalid_data)
#         form = response.context["form"]

#         self.assertEqual(response.status_code, 200)
#         self.assertFalse(User.objects.filter(username=invalid_data["username"]).exists())
#         self.assertFalse(form.is_valid())
#         self.assertIn("このパスワードは ユーザー名 と似すぎています。", form.errors["password2"])

#     # Test Case 11
#     def test_failure_post_with_only_numbers_password(self):
#         invalid_data = {
#             "username": "testuser",
#             "email": "test@test.com",
#             "password1": "11111111",
#             "password2": "11111111",
#         }
#         response = self.client.post(self.url, invalid_data)
#         form = response.context["form"]

#         self.assertEqual(response.status_code, 200)
#         self.assertFalse(User.objects.filter(username=invalid_data["username"]).exists())
#         self.assertFalse(form.is_valid())
#         self.assertIn("このパスワードは数字しか使われていません。", form.errors["password2"])

#     # Test Case 12
#     def test_failure_post_with_mismatch_password(self):
#         invalid_data = {
#             "username": "testuser",
#             "email": "test@test.com",
#             "password1": "testpassword",
#             "password2": "testdayo",
#         }
#         response = self.client.post(self.url, invalid_data)
#         form = response.context["form"]

#         self.assertEqual(response.status_code, 200)
#         self.assertFalse(User.objects.filter(username=invalid_data["username"]).exists())
#         self.assertFalse(form.is_valid())
#         self.assertIn("確認用パスワードが一致しません。", form.errors["password2"])


# class TestLoginView(TestCase):
#     def setUp(self):
#         self.url = reverse("accounts:login")
#         self.user = User.objects.create_user(
#             username="testuser",
#             email="test@example.com",
#             password="testpassword",
#         )

#     # Test Case 2-2
#     def test_success_get(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, "accounts/login.html")

#     # Test Case 2-3
#     def test_success_post(self):
#         valid_data = {
#             "username": "testuser",
#             "password": "testpassword",
#         }
#         response = self.client.post(self.url, valid_data)

#         self.assertRedirects(
#             response,
#             reverse(settings.LOGIN_REDIRECT_URL),
#             status_code=302,
#             target_status_code=200,
#         )
#         self.assertIn(SESSION_KEY, self.client.session)

#     # Test Case 2-4
#     def test_failure_post_with_not_exists_user(self):
#         invalid_data = {
#             "username": "testuser2",
#             "password": "testpassword",
#         }
#         response = self.client.post(self.url, invalid_data)
#         form = response.context["form"]

#         self.assertEqual(response.status_code, 200)
#         self.assertFalse(form.is_valid())
#         self.assertNotIn(SESSION_KEY, self.client.session)
#         self.assertIn(
#             "正しいユーザー名とパスワードを入力してください。どちらのフィールドも大文字と小文字は区別されます。",
#             form.errors["__all__"],
#         )

#     # Test Case 2-5
#     def test_failure_post_with_empty_password(self):
#         invalid_data = {
#             "username": "testuser",
#             "password": "",
#         }
#         response = self.client.post(self.url, invalid_data)
#         form = response.context["form"]

#         self.assertEqual(response.status_code, 200)
#         self.assertFalse(form.is_valid())
#         self.assertNotIn(SESSION_KEY, self.client.session)
#         self.assertIn("このフィールドは必須です。", form.errors["password"])


# class TestLogoutView(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username="testuser", password="testpassword")
#         self.client.login(username="testuser", password="testpassword")

#     # Test Case 2-6
#     def test_success_post(self):
#         self.url = reverse("accounts:logout")
#         response = self.client.post(self.url)
#         print(response)
#         self.assertRedirects(
#             response,
#             reverse(settings.LOGOUT_REDIRECT_URL),
#             status_code=302,
#             target_status_code=200,
#         )
#         self.assertNotIn(SESSION_KEY, self.client.session)


class TestUserProfileView(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="testpassword")
        self.client.login(username="tester", password="testpassword")
        self.tweet = Model.objects.create(body="test", creator=self.user)
        self.client.logout()
        self.user2 = User.objects.create_user(username="tester2", password="testpassword")
        self.client.login(username="tester2", password="testpassword")
        self.tweet = Model.objects.create(body="test2", creator=self.user2)

    # Case 3-2
    def test_success_get(self):
        url = reverse("accounts:user_profile", kwargs={"username": self.user.username})
        response = self.client.get(url)
        tweet_context = response.context["tweets"]
        true_context = Model.objects.filter(creator__username=self.user)
        self.assertQuerysetEqual(tweet_context, true_context, ordered=False)


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
