FROM python:3.11-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /django

# Install system dependencies 
RUN apk update && apk add --no-cache \
    build-base \
    mariadb-dev \
    python3-dev \
    libstdc++ \
    alsa-lib-dev \
    portaudio-dev \
    libffi-dev

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Run migrations as part of the build process 
RUN  python manage.py makemigrations
RUN  python manage.py migrate 
# RUN  python manage.py test customer.tests

# Create a superuser (admin) 
RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('root', 'root@gmail.com', 'root@123')" | python manage.py shell

# Expose the port for Django development server
EXPOSE 8000

# Default command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
