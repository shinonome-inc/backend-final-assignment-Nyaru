# from django.contrib.auth import get_user_model
# from django.test import TestCase
# from django.urls import reverse

# from .models import Tweet

# User = get_user_model()
# Model = Tweet

# # Case 1-02(response) & 3-01(model_data)
# class TestHomeView(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username="tester", password="testpassword")
#         self.client.login(username="tester", password="testpassword")

# # Case 1-02 ,3-01
# def test_success_get(self):
#     response = self.client.get(reverse("tweets:home"))
#     self.assertEqual(response.status_code, 200)
#     self.assertTemplateUsed(response, "tweets/home.html")
#     tweet_context = response.context["object_list"]
#     true_context = Model.objects.all()
#     self.assertQuerysetEqual(tweet_context, true_context, ordered=False)


# # Case 3-03, 3-04, 3-05, 3-06
# class TestTweetCreateView(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username="tester", password="testpassword")
#         self.client.login(username="tester", password="testpassword")
#         self.base_records = Model.objects.all()
#         self.count = Model.objects.count()

#     # 3-03
#     def test_success_get(self):
#         response = self.client.get(reverse("tweets:create"))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, "tweets/create.html")

#     # 3-04
#     def test_success_post(self):
#         data = {
#             "body": "test content",
#         }
#         response = self.client.post(reverse("tweets:create"), data)
#         self.assertRedirects(
#             response,
#             reverse("tweets:home"),
#             status_code=302,
#             target_status_code=200,
#         )
#         self.assertEqual(Model.objects.count(), self.count + 1)
#         self.assertEqual(Model.objects.last().body, data["body"])

#     # 3-05
#     def test_failure_post_with_empty_content(self):
#         data = {
#             "body": "",
#         }
#         response = self.client.post(reverse("tweets:create"), data)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, "tweets/create.html")
#         self.assertEqual(response.context["form"].errors, {"body": ["ツイート内容がありませんわ～！"]})
#         self.assertQuerySetEqual(Model.objects.all(), self.base_records)

#     # 3-06
#     def test_failure_post_with_too_long_content(self):
#         data = {
#             "body": "a" * 141,
#         }
#         response = self.client.post(reverse("tweets:create"), data)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, "tweets/create.html")
#         self.assertEqual(response.context["form"].errors, {"body": ["ツイートが140字を超えていますわ～！"]})
#         self.assertQuerySetEqual(Model.objects.all(), self.base_records)


# # Case 3-07
# class TestTweetDetailView(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username="tester1", password="testpassword")
#         self.client.login(username="tester1", password="testpassword")
#         self.tweet1 = Model.objects.create(body="test content", creator=self.user)
#         self.tweet2 = Model.objects.create(body="test content2", creator=self.user)

#     # 3-07
#     def test_success_get(self):
#         response = self.client.get(reverse("tweets:detail", kwargs={"pk": self.tweet1.pk}))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, "tweets/detail.html")
#         self.assertEqual(response.context["tweet"], Model.objects.get(pk=self.tweet1.pk))


# # Case 3-08, 3-09, 3-10
# class TestTweetDeleteView(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username="tester", password="testpassword")
#         self.client.login(username="tester", password="testpassword")
#         self.tweet1 = Model.objects.create(body="test content", creator=self.user)
#         self.tweet2 = Model.objects.create(body="test content2", creator=self.user)
#         self.count = Model.objects.count()
#         self.base_records = Model.objects.all()

#     # 3-08
#     def test_success_post(self):
#         response = self.client.post(reverse("tweets:delete", kwargs={"pk": self.tweet1.pk}))
#         self.assertRedirects(
#             response,
#             reverse("tweets:home"),
#             status_code=302,
#             target_status_code=200,
#         )
#         self.assertQuerysetEqual(Model.objects.all(), self.base_records.exclude(pk=self.tweet1.pk))

#     # 3-09
#     def test_failure_post_with_not_exist_tweet(self):
#         response = self.client.post(reverse("tweets:delete", kwargs={"pk": 100}))
#         self.assertEqual(response.status_code, 404)
#         self.assertQuerySetEqual(Model.objects.all(), self.base_records, ordered=False)

#     # 3-10
#     def test_failure_post_with_incorrect_user(self):
#         User.objects.create_user(username="tester2", password="testpassword")
#         self.client.login(username="tester2", password="testpassword")
#         response = self.client.post(reverse("tweets:delete", kwargs={"pk": self.tweet1.pk}))
#         self.assertEqual(response.status_code, 403)
#         self.assertQuerySetEqual(Model.objects.all(), self.base_records, ordered=False)


# # # class TestLikeView(TestCase):
# # #     def test_success_post(self):

# # #     def test_failure_post_with_not_exist_tweet(self):

# # #     def test_failure_post_with_liked_tweet(self):


# # # class TestUnLikeView(TestCase):

# # #     def test_success_post(self):

# # #     def test_failure_post_with_not_exist_tweet(self):

# # #     def test_failure_post_with_unliked_tweet(self):
