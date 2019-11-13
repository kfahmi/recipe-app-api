from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

	def test_create_user_with_email_successful(self):
		"""Test creating user with email"""
		email = 'test@fahmi.com'
		password  = 'testpass123'
		user = get_user_model().objects.create_user(
			email=email,
			password=password
		)

		self.assertEqual(user.email, email)
		self.assertTrue(user.check_password(password))


	def test_new_user_email_normalized(self):
		"""Test email for a new user normalized"""
		email = "test@LonDOnAppDev.Com"
		user = get_user_model().objects.create_user(email,'test123')

		self.assertEqual(user.email, email.lower())


	def test_new_user_invalid_email(self):
		"""test create user with no email raise error"""
		with self.assertRaises(ValueError):
			get_user_model().objects.create_user(None,'test123')



	def test_create_new_superuser(self):
		"""Test creating new superuser"""
		user = get_user_model().objects.create_superuser(
			'test@fahmi.com'
			'test123'
			)

		self.assertTrue(user.is_superuser)
		self.assertTrue(user.is_staff)