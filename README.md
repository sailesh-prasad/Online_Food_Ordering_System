# Food Ordering System

## Introduction
The goal of this project is to streamline the interaction between customers and restaurants, improving the online food ordering experience. The platform will enable customers to search for restaurants, browse menus, place orders, and track their deliveries in real-time. For restaurants, it will provide a system to manage orders, assign delivery personnel, and offer live updates on order status. The platform will also integrate delivery management features, including real-time tracking and geolocation data capture, as well as email notifications for user registration, login, and order updates.

## Key Features
- User registration and authentication
- Browse and search for restaurants
- Add items to the cart and place orders
- Track order status
- Admin panel for managing restaurants and orders
### **Customer Features:**
1. **Restaurant Search**: Customers can search for restaurants based on name, cuisine, or location.
2. **Menu Browsing**: View menu items, including descriptions and prices.
3. **Order Placement**: Select items and place an order, with customizable options.
4. **Order Tracking**: Real-time updates on order status and live map tracking of deliveries.

### **Restaurant Features:**
1. **Order Management**: Restaurants can accept or decline incoming orders (e.g., "Out of Stock").
2. **Assign Delivery Personnel**: Allocate orders to specific delivery drivers.
3. **Order Status Updates**: Provide real-time updates to customers regarding their order (e.g., "In Progress," "Out for Delivery").

### **Delivery Features:**
1. **Geolocation**: Capture and store real-time location data for deliveries.
2. **Live Updates**: Provide real-time map updates to customers.

## Project Scope
### **For Customers:**
- **Search for Restaurants**: Customers can search for restaurants by name, cuisine, or location.
- **Browse Menus**: Customers can view menu items and select their desired food.
- **Real-Time Order Tracking**: Customers can view the delivery status and estimated arrival time.
- **Email Notifications**: Customers will receive confirmation emails upon order placement and successful delivery.

### **For Restaurants:**
- **View and Manage Orders**: Restaurants can view incoming orders, accept or decline them, and track order statuses.
- **Assign Delivery Personnel**: Allocate delivery tasks to available drivers based on proximity.
- **Update Order Status**: Provide real-time updates on order progress, such as “Preparing”, “Out for Delivery”.

### **Delivery Management:**
- **Geolocation Tracking**: Real-time tracking of the delivery agent’s location during delivery.
- **Live Map-based Updates**: Display delivery progress on a map in real-time for both customers and restaurant staff. 

## Requirements
### **Functional Requirements**
#### **Customers:**
- Ability to search for restaurants.
- View restaurant menus and place orders.
- Real-time tracking of orders.
- Receive email notifications about registration, login, and order delivery.

#### **Restaurants:**
- Ability to view, accept, or decline orders.(e.g., "Out Of Stock")
- Assign delivery personnel to specific orders.
- Update order statuses (e.g., "Confirmed", "Out for Delivery").

#### **Delivery Management:**
- Record geolocation data for delivery personnel.
- Display live map-based tracking for users and restaurants.

### **Non-Functional Requirements**
- **Usability**: Intuitive and easy-to-use interface for both customers and restaurants.
- **High Availability**: The system must be accessible 24/7 with minimal downtime.
- **Data Security**: Protection of customer, restaurant, and order data.

## Technologies Used
- Frontend: HTML, CSS, JavaScript, Bootstrap
- Backend: Django
- Database: PostgreSQL
- Deployment: Docker

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/pythonandspring/Food-ordering.git

2. Navigate to the project directory:
   ```bash
   cd Food-ordering

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Run database migrations:
   ```bash
   python manage.py migrate

5. Start the development server:
   ```bash
   python manage.py runserver

## For Testing
1. Run test command:
   ```bash
   python manage.py test

## For API Swagger
1. Check the URL:
   ```bash
   localhost:8000/api/swagger/

## Development Workflow
### **1. Initial Setup:**
- Set up the Django project and configure SQLite for initial development.
- Initialize the Git repository and connect it to GitHub for version control.

### **2. Frontend Development:**
- Design and build responsive web pages using JavaScript.
- Integrate API calls for fetching restaurant data, placing orders, and tracking deliveries.

### **3. Backend Development:**
- Create Django models for users, restaurants, orders, and delivery tracking.
- Build views and serializers to serve data to the frontend via the Django REST framework.

### **4. Deployment:**
- Containerize the application using Docker to ensure consistency across environments.
- Test the application thoroughly before deploying to cloud platforms (e.g., Docker).

## Screenshots
**Homepage**:
![Screenshot 2024-12-27 173503](https://github.com/user-attachments/assets/522d3aee-8906-4ee3-b396-ab1f1358000a)
![Screenshot 2024-12-27 173532](https://github.com/user-attachments/assets/ad20ea88-ccd8-41ef-adf9-040e70c465fb)
**Customer Login Page**:
![Screenshot 2024-12-27 173635](https://github.com/user-attachments/assets/f054e8f8-2e80-4f55-bec5-c25a962b60fc)
**Customer Registration Page**:
![Screenshot 2024-12-27 173654](https://github.com/user-attachments/assets/d0a6dc2c-d32c-468a-a00e-a1b08bd3e000)
![Screenshot 2024-12-27 173721](https://github.com/user-attachments/assets/812a94f4-1b63-492c-b169-57539802280b)
**Customer Welcome Page**:
![Screenshot 2024-12-27 174256](https://github.com/user-attachments/assets/85f7ae1b-bdea-4fd2-86c0-e88e454691a3)
![Screenshot 2024-12-27 174413](https://github.com/user-attachments/assets/3e116fb3-7a4e-49cc-a381-67b4cbb7d1f8)
**Restaurant Login Page**:
![Screenshot 2024-12-27 174503](https://github.com/user-attachments/assets/0e087554-8506-49be-80da-ed426c693bd8)
**Restaurant Registration Page**:
![Screenshot 2024-12-27 174521](https://github.com/user-attachments/assets/a8dcceb7-d282-487e-bdf4-2feeae5310e6)
![Screenshot 2024-12-27 174534](https://github.com/user-attachments/assets/9a21bc97-7278-4df6-9310-4957441398d5)
**Restaurant Welcome Page**:
![Screenshot 2024-12-27 174656](https://github.com/user-attachments/assets/cef3286d-468c-45f2-a8b7-9154edaf0554)
![Screenshot 2024-12-27 174708](https://github.com/user-attachments/assets/6bfc0502-109d-48cf-b8f6-8be24a972625)
**Delivery Person Login Page**:
![Screenshot 2024-12-27 174849](https://github.com/user-attachments/assets/b9f5185c-f109-4232-a3c4-100da6b4ea0e)
**Delivery Person Registration Page**:
![Screenshot 2024-12-27 174902](https://github.com/user-attachments/assets/9f2565e7-49a3-40d1-b926-50761735fe02)
![Screenshot 2024-12-27 174916](https://github.com/user-attachments/assets/4f8d70dd-4c3d-4ea7-99de-b656001ae4b1)
**Delivery Person Welcome Page**:
![Screenshot 2024-12-27 175402](https://github.com/user-attachments/assets/52556393-f408-46ec-b27a-b7bad31156a2)
**Feedback Form**:
![Screenshot 2024-12-27 174139](https://github.com/user-attachments/assets/5c435e0b-73e5-41c1-97c8-eff3a976158f)

## Future Enhancements
1. **Payment Integration**: Integrate secure online payment gateways (e.g., Stripe or PayPal) to handle transactions directly through the platform.
2. **Advanced Analytics**: Provide restaurants with analytics on customer preferences, best-selling items, and order trends.
