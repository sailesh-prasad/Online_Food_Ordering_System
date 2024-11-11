from django.test import TestCase
from customer.models import Customer
from django.core.exceptions import ValidationError

# Customer model tests
class CustomerModelTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            CustomerFName="John",
            CustomerLName="Doe",
            CustomerCont="1234567890",
            CustomerEmail="john.doe@example.com",
            CustomerPass="password123",
            Address="123 Main St"
        )

    def test_customer_creation(self):
        self.assertIsInstance(self.customer, Customer)
        self.assertEqual(self.customer.CustomerFName, "John")
        self.assertEqual(self.customer.CustomerLName, "Doe")
        self.assertEqual(self.customer.CustomerCont, "1234567890")
        self.assertEqual(self.customer.CustomerEmail, "john.doe@example.com")
        self.assertEqual(self.customer.CustomerPass, "password123")
        self.assertEqual(self.customer.Address, "123 Main St")

    def test_customer_str(self):
        expected_str = f"{self.customer.CustomerFName} {self.customer.CustomerLName}"
        self.assertEqual(str(self.customer), expected_str)

    def test_required_fields(self):
        with self.assertRaises(ValidationError):
            Customer.objects.create(
                CustomerFName="",
                CustomerLName="",
                CustomerCont="",
                CustomerEmail="",
                CustomerPass="",
                Address=""
            ).full_clean()

    def test_field_lengths(self):
        customer = Customer.objects.create(
            CustomerFName="A" * 30,
            CustomerLName="B" * 30,
            CustomerCont="1" * 10,
            CustomerEmail="email@example.com",
            CustomerPass="password123",
            Address="C" * 150
        )
        customer.full_clean()  # Should not raise any exceptions

    def test_unique_email(self):
        Customer.objects.create(
            CustomerFName="Jane",
            CustomerLName="Doe",
            CustomerCont="0987654321",
            CustomerEmail="jane.doe@example.com",
            CustomerPass="password123",
            Address="456 Another St"
        )
        with self.assertRaises(ValidationError):
            duplicate_customer = Customer(
                CustomerFName="Jane",
                CustomerLName="Doe",
                CustomerCont="0987654321",
                CustomerEmail="jane.doe@example.com",
                CustomerPass="password123",
                Address="456 Another St"
            )
            duplicate_customer.full_clean()

    def test_default_address(self):
        customer = Customer.objects.create(
            CustomerFName="Default",
            CustomerLName="Address",
            CustomerCont="1234567890",
            CustomerEmail="default.address@example.com",
            CustomerPass="password123"
        )
        self.assertEqual(customer.Address, "")