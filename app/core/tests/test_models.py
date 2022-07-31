"""
Tests for custom models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test class for custom models"""

    def test_create_user_success(self):
        """Test if user creation is successful with email and password"""
        email = "test1@example.com"
        password = "test1pass"

        user_model_object = get_user_model().objects
        user = user_model_object.create_user(
            email=email, password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalize(self):
        """Test if user email is normalized"""
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["TEST2@EXAMPLE.COM", "TEST2@example.com"],
            ["Test3@example.com", "Test3@example.com"],
        ]
        user_model_object = get_user_model().objects

        for original_email, normalized_email in sample_emails:
            user = user_model_object.create_user(
                email=original_email, password='test0pass'
            )
            self.assertEqual(user.email, normalized_email)

    def test_create_user_without_email_password_fails(self):
        """Test if user creation is failed with empty email and password"""
        user_model_object = get_user_model().objects

        with self.assertRaises(ValueError):
            user_model_object.create_user(email="", password="test123")
        with self.assertRaises(ValueError):
            user_model_object.create_user(
                email="test1@example.com", password=""
            )

    def test_create_super_user_success(self):
        """Test if superuser is created"""
        user_model_object = get_user_model().objects
        super_user = user_model_object.create_superuser(
            email="test1@example.com", password="test1super"
        )

        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
