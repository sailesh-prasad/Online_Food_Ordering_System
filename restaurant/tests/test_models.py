from django.test import TestCase
from customer.models import Restaurant
from django.core.exceptions import ValidationError

class RestaurantModelTest(TestCase):

    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name="Test Restaurant",
            address="123 Test St",
            phone_number="1234567890",
            email="test@example.com",
            opening_hours="9 AM - 9 PM",
            cuisine_type="Italian",
            rating=4.5,
            website_url="http://www.testrestaurant.com"
        )

    def test_restaurant_creation(self):
        self.assertIsInstance(self.restaurant, Restaurant)
        self.assertEqual(self.restaurant.name, "Test Restaurant")
        self.assertEqual(self.restaurant.address, "123 Test St")
        self.assertEqual(self.restaurant.phone_number, "1234567890")
        self.assertEqual(self.restaurant.email, "test@example.com")
        self.assertEqual(self.restaurant.opening_hours, "9 AM - 9 PM")
        self.assertEqual(self.restaurant.cuisine_type, "Italian")
        self.assertEqual(self.restaurant.rating, 4.5)
        self.assertEqual(self.restaurant.website_url, "http://www.testrestaurant.com")

    def test_restaurant_str(self):
        self.assertEqual(str(self.restaurant), "Test Restaurant")

    def test_default_address(self):
        restaurant = Restaurant.objects.create(
            name="Default Address Restaurant"
        )
        self.assertEqual(restaurant.address, "Unknown Address")

    def test_optional_fields(self):
        restaurant = Restaurant.objects.create(
            name="Optional Fields Restaurant"
        )
        self.assertIsNone(restaurant.phone_number)
        self.assertIsNone(restaurant.email)
        self.assertIsNone(restaurant.opening_hours)
        self.assertIsNone(restaurant.cuisine_type)
        self.assertIsNone(restaurant.rating)
        self.assertIsNone(restaurant.website_url)

    def test_field_lengths(self):
        restaurant = Restaurant.objects.create(
            name="A" * 100,
            address="B" * 255,
            phone_number="1" * 15,
            email="email@example.com",
            opening_hours="C" * 100,
            cuisine_type="D" * 50,
            rating=4.5,
            website_url="http://www.example.com"
        )
        restaurant.full_clean()  # Should not raise any exceptions

    def test_invalid_rating(self):
        with self.assertRaises(ValidationError):
            restaurant = Restaurant(
                name="Invalid Rating Restaurant",
                rating=10.0  # Invalid rating, should be between 0 and 5
            )
            restaurant.full_clean()