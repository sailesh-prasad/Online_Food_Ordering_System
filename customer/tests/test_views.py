from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from customer.models import Feedback, Contact

class ViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')

    def test_login_view_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/login.html')

    def test_login_view_post(self):
        response = self.client.post(reverse('login'), {'email': 'testuser', 'password': 'testpassword'})
        self.assertRedirects(response, reverse('menu'))

    def test_login_view_invalid_credentials(self):
        response = self.client.post(reverse('login'), {'email': 'wronguser', 'password': 'wrongpassword'})
        self.assertRedirects(response, reverse('login'))
        self.assertContains(response, 'Invalid Password or Username', status_code=200)

    def test_register_view_get(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/register.html')

    def test_register_view_post(self):
        response = self.client.post(reverse('register'), {'name': 'newuser', 'email': 'newuser@example.com', 'password': 'newpassword'})
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(get_user_model().objects.filter(username='newuser@example.com').exists())

    def test_register_view_existing_user(self):
        response = self.client.post(reverse('register'), {'name': 'testuser', 'email': 'testuser', 'password': 'testpassword'})
        self.assertRedirects(response, reverse('login'))
        self.assertContains(response, 'User Already Exist in the System', status_code=200)

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/logout.html')

    def test_feedback_form_view_get(self):
        response = self.client.get(reverse('feedback'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feedback.html')

    def test_feedback_form_view_post(self):
        response = self.client.post(reverse('feedback'), {'comment': 'Great service!'})
        self.assertTemplateUsed(response, 'thank_you.html')
        self.assertTrue(Feedback.objects.filter(comments='Great service!').exists())

    def test_contact_form_view_get(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_contact_form_view_post(self):
        response = self.client.post(reverse('contact'), {'name': 'John Doe', 'email': 'john@example.com', 'subject': 'Inquiry'})
        self.assertTemplateUsed(response, 'thank_you.html')
        self.assertTrue(Contact.objects.filter(email='john@example.com').exists())

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')