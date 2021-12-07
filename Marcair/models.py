from django.db import models
from django.db.models.fields import PositiveIntegerField
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

# Database Models

class Airport(models.Model):
    # champs
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=100,help_text='ex : France')
    airport_name = models.CharField(max_length=100, help_text='ex : aéroport Charles de Gaulle')
    code = models.CharField(max_length=3, help_text='ex : CDG')
    # méthodes
    def __str__(self):
        return f'{self.airport_name}, {self.code}'
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('airport-details', args=[str(self.id)])

class Airplane(models.Model):
    # champs
    id = models.AutoField(primary_key=True)
    immatriculation = models.CharField(max_length=30, unique=True)
    type = models.CharField(max_length=100, help_text='ex : Boeing 777')
    # méthodes
    def __str__(self):
        return f'{self.immatriculation}, {self.type}'
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('airplane-details', args=[str(self.id)])

class Connection(models.Model):
    # champs
    id =  models.AutoField(primary_key=True)
    arrival_airport_id = models.ForeignKey('Airport', on_delete=models.SET_NULL, null=True, related_name='arrival')
    departure_airport_id = models.ForeignKey('Airport', on_delete=models.SET_NULL, null=True, related_name='departure') 
    # méthodes
    def __str__(self):
        return f'{self.departure_airport_id}, {self.arrival_airport_id}'
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('connection-details', args=[str(self.id)])

class Employee(models.Model):
    # champs
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, help_text='ex : Marc')
    last_name = models.CharField(max_length=100, help_text='ex : Cohen')
    adress = models.CharField(max_length=100, help_text='ex : 16 rue de la paix, 75000 Paris')
    salary = models.PositiveIntegerField()
    security_number = models.CharField(max_length=30, unique=True)
    # méthode
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('employee-details', args=[str(self.id)])
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

class Client(models.Model):
    # champs
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, help_text='ex : Pierre')
    last_name = models.CharField(max_length=100, help_text='ex : Niney')
    client_adress = models.CharField(max_length=100, help_text='ex : 16 rue de la paix, 75000 Paris')
    client_email_adress = models.EmailField(help_text='ex : pierre.niney@gmail.com')
    # méthode 
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('customer-details', args=[str(self.id)])
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name},{self.id},{self.client_email_adress} '

class Pilot(models.Model):
    # champs
    id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, related_name='pilot')
    license_number = models.PositiveIntegerField(unique=True)
    # méthode 
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('customer-details', args=[str(self.id)])
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.employee_id},{self.license_number} '

class CrewMember(models.Model):
    # champs
    id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, related_name='crew')
    role = models.CharField(max_length=30, help_text='ex : Stewart, Hotesse')
    # méthode 
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('crew-details', args=[str(self.id)])
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.employee_id},{self.role} '

class Flight(models.Model):
    # champs
    id = models.AutoField(primary_key=True)
    flight_number = models.PositiveIntegerField(unique=True)
    connection_id = models.ForeignKey('Connection',on_delete=models.SET_NULL, null=True, related_name='connection_flight')
    airplane_id = models.ForeignKey('Airplane',on_delete=models.SET_NULL, null=True, related_name='airplane_flight')
    departure_id = models.ForeignKey('Departure',on_delete=models.SET_NULL, null=True, related_name='departure_id')
    departure_day = models.DateField()
    arrival_day = models.DateField()
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    # méthode 
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('flight-details', args=[str(self.id)])
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.flight_number},{self.departure_day}, {self.departure_time} '

class Departure(models.Model):
    # champs
    id = models.AutoField(primary_key=True)
    flight_id = models.ForeignKey('Flight',on_delete=models.SET_NULL, null=True, related_name='flight_departure')
    pilot_id = models.ForeignKey('Pilot',on_delete=models.SET_NULL, null=True, related_name='pilot_departure')
    optional_pilot_id = models.ForeignKey('Pilot',on_delete=models.SET_NULL, null=True, related_name='copilot')
    first_crew_member_id = models.ForeignKey('CrewMember',on_delete=models.SET_NULL, null=True, related_name='crew1')
    second_crew_member_id = models.ForeignKey('CrewMember',on_delete=models.SET_NULL, null=True, related_name='crew2', blank=True)
    number_of_empty_seat = PositiveIntegerField()
    number_of_reserved_seat = PositiveIntegerField()
    # méthode 
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('departure-details', args=[str(self.id)])
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.flight_id},{self.number_of_empty_seat}'

class Ticket(models.Model):
    # champs
    id = models.AutoField(primary_key=True)
    ticket_number = models.PositiveIntegerField(unique=True)
    date_time_of_issue = models.DateTimeField()
    price = models.PositiveIntegerField()
    departure_id = models.ForeignKey('Departure',on_delete=models.SET_NULL, null=True, related_name='departure_ticket')
    client_id = models.ForeignKey('Client',on_delete=models.SET_NULL, null=True, related_name='client_ticket')
    # méthode 
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('ticket-details', args=[str(self.id)])
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.ticket_number},{self.date_time_of_issue}, {self.price}'

class Transaction(models.Model):
    # champs
    id = models.AutoField(primary_key=True)
    transaction_number = models.PositiveIntegerField(unique=True)
    ticket_id = models.ForeignKey('Ticket',on_delete=models.CASCADE, null=True, related_name='ticket_transaction')
    id_client = models.ForeignKey('Client',on_delete=models.CASCADE, null=True, related_name='client_transaction')
    # méthode
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('transaction-details', args=[str(self.id)])
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.transaction_number},{self.id_client}, {self.ticket_id}'

# Extra classes to manage the use of the website
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, last_name=None, first_name=None, adress=None):
        # add a client or an employee when we add a user 
        if not email:
            raise ValueError("Vous devez rentrer un email")

        user = self.model(
            email=self.normalize_email(email),
            last_name=last_name,
            first_name=first_name,
            adress=adress,
            )
        user.set_password(password)
        user.save()
        return user

    def create_super_user(self, email, password=None, last_name=None, first_name=None, adress=None):
        user = self.create_user(email=email, password=password, last_name=last_name, first_name=first_name, adress=adress)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user
