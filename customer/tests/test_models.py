from django.test import TestCase
from customer.models import Customer,Food 
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
        
        
        
#! food model test cases 

class FoodModelTest(TestCase):

    def setUp(self):
        self.food = Food.objects.create(
            FoodName="Pizza",
            FoodCat="Fast Food",
            FoodPrice=9.99,
            FoodImage="media/pizza.jpg"
        )

    def test_food_creation(self):
        self.assertIsInstance(self.food, Food)
        self.assertEqual(self.food.FoodName, "Pizza")
        self.assertEqual(self.food.FoodCat, "Fast Food")
        self.assertEqual(self.food.FoodPrice, 9.99)
        self.assertEqual(self.food.FoodImage, "media/pizza.jpg")

    def test_food_str(self):
        expected_str = f"{self.food.FoodName}"
        self.assertEqual(str(self.food), expected_str)

    def test_field_lengths(self):
        food = Food.objects.create(
            FoodName="A" * 30,
            FoodCat="B" * 30,
            FoodPrice=19.99,
            FoodImage="media/food.jpg"
        )
        food.full_clean()  # Should not raise any exceptions

    def test_default_food_image(self):
        food = Food.objects.create(
            FoodName="Burger",
            FoodCat="Fast Food",
            FoodPrice=5.99
        )
        self.assertEqual(food.FoodImage, "")

    def test_food_price_validation(self):
        with self.assertRaises(ValidationError):
            food = Food(
                FoodName="Invalid Price",
                FoodCat="Fast Food",
                FoodPrice="invalid_price"
            )