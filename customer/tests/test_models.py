from django.test import TestCase
from customer.models import Customer


#customer model tests 
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
        
        
#