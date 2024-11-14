from django.test import TestCase
from customer.models import Ordering
from django.core.exceptions import ValidationError

class OrderingModelTest(TestCase):

    def setUp(self):
        self.ordering = Ordering.objects.create(
            name="Test Ordering",
            address="123 Test St",
            phone_number=1234567890,
            email="test@example.com"
        )

    def test_ordering_creation(self):
        self.assertIsInstance(self.ordering, Ordering)
        self.assertEqual(self.ordering.name, "Test Ordering")
        self.assertEqual(self.ordering.address, "123 Test St")
        self.assertEqual(self.ordering.phone_number, 1234567890)
        self.assertEqual(self.ordering.email, "test@example.com")

    def test_ordering_str(self):
        self.assertEqual(str(self.ordering), "Test Ordering")

    def test_required_fields(self):
        with self.assertRaises(ValidationError):
            Ordering.objects.create(
                address="",
                phone_number=None,
                email=""
            ).full_clean()

    def test_field_lengths(self):
        ordering = Ordering.objects.create(
            name="A" * 100,
            address="B" * 255,
            phone_number=1234567890,
            email="email@example.com"
        )
        ordering.full_clean()  # Should not raise any exceptions

    def test_invalid_phone_number(self):
        with self.assertRaises(ValidationError):
            ordering = Ordering(
                name="Invalid Phone Number",
                address="123 Test St",
                phone_number="invalid_phone_number",
                email="test@example.com"
            )
            ordering.full_clean()