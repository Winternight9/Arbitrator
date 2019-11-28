from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.shortcuts import render,reverse


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = "testuser"
        self.userpass = "123$*HCfjdksla"
        self.user = User.objects.create_user(self.username,password=self.userpass)

    def test_index(self):
        c = self.client
        response = c.get(path='')
        status = response.status_code
        self.assertEqual(status, 200)

    def test_index_template(self):
        c = self.client
        response = c.get(path='')
        self.assertTemplateUsed(response, 'arbitrator/index.html')

    def test_signup(self) :
        c = self.client
        response = c.get(path='/register/')
        status = response.status_code
        self.assertEqual(status, 200)

    def test_signup_template(self):
        c = self.client
        response = c.get(path='/register/')
        self.assertTemplateUsed(response, 'arbitrator/registration.html')

    def test_homepage(self):
        c = self.client
        response = c.get(path='/home/')
        status = response.status_code
        self.assertEqual(status, 200)

    def test_homepage_template(self):
        c = self.client
        response = c.get(path='/home/')
        self.assertTemplateUsed(response, 'arbitrator/home.html')

    def test_profile_not_logged_in(self):
        c = self.client
        response = c.get(path='/profile/')
        status = response.status_code
        self.assertEqual(status, 302)

    def test_edit_profile_not_logged_in(self):
        c = self.client
        response = self.client.get(path='/profile/edit')
        status = response.status_code
        self.assertEqual(status, 301)

    def test_profile_logged_in(self):
        self.client.force_login(self.user)
        response = self.client.get(path='/profile/')
        status = response.status_code
        self.assertEqual(status, 200)

    def test_edit_profile_logged_in(self):
        self.client.force_login(self.user)
        response = self.client.get(path='/profile/edit/')
        status = response.status_code
        self.assertEqual(status, 200)

    def test_profile_template(self):
        self.client.force_login(self.user)
        response = self.client.get(path='/profile/')
        self.assertTemplateUsed(response, 'arbitrator/profile.html')

    def test_user_can_login(self):
        response = self.client.post('/login/',
            {'username':self.user.username, 'password':self.userpass})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('arbitrator:home'))