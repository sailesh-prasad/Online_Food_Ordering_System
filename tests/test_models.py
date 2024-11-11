from django.test import TestCase
from customer.models import Student

class StudentModelTest(TestCase):

    def setUp(self):
        #! create a test instance
        self.student = Student.objects.create(
            first_name='John',
            last_name='Doe',
            father_name='Father Doe',
            mother_name='Mother Doe',
            student_class='1st',
            phone_number='1234567890',
            address='123 Main St',
            email='john.doe@example.com',
            date_of_join='2023-01-01',
            date_of_leaving='2023-12-31',
            second_phone_number='0987654321',
            photo=None,
            identity_marks='Mole on left cheek',
            aadhar_number='1234-5678-9012',
            birth_certificate_number='BC123456'
        )

    def test_student_creation(self):
        #! test student creation
        self.assertEqual(self.student.first_name, 'John')
        self.assertEqual(self.student.last_name, 'Doe')
        self.assertEqual(self.student.father_name, 'Father Doe')
        self.assertEqual(self.student.mother_name, 'Mother Doe')
        self.assertEqual(self.student.student_class, '1st')
        self.assertEqual(self.student.phone_number, '1234567890')
        self.assertEqual(self.student.address, '123 Main St')
        self.assertEqual(self.student.email, 'john.doe@example.com')
        self.assertEqual(self.student.date_of_join, '2023-01-01')
        self.assertEqual(self.student.date_of_leaving, '2023-12-31')

    def test_student_str_method(self):
        
        self.assertEqual(str(self.student), 'John Doe')
        
    from django.test import TestCase
    
    
    
    
class CustomerModelTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            name='Wasabi',
            address='123 westford',
            phNo='1234567891',
            email='123@gmail.com'
        )

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, 'Wasabi')
        self.assertEqual(self.customer.address, '123 westford')
        self.assertEqual(self.customer.phNo, '1234567891')
        self.assertEqual(self.customer.email, '123@gmail.com')
	
    