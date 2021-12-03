from django.contrib import admin

from Marcair.models import Airport, Airplane, Employee, Connection, Pilot, Transaction, Departure, Flight, Ticket, CrewMember, Client

# admin.site.register(Airport)
# admin.site.register(Airplane)
# admin.site.register(Employee)
admin.site.register(Connection)
# admin.site.register(Transaction)
# admin.site.register(Pilot)
# admin.site.register(CrewMember)
# admin.site.register(Departure)
# admin.site.register(Flight)
# admin.site.register(Ticket)
# admin.site.register(Client)

# Define the admin class to have a list view in the admin environment
class PilotAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee_id', 'license_number')
    fields = ['employee_id','license_number']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','last_name', 'first_name', 'adress', 'security_number','salary')
    fields = [('first_name', 'last_name'), 'adress', 'security_number','salary']

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id','last_name', 'first_name', 'client_adress')
    fields = [('first_name', 'last_name'), 'client_adress',]

class CrewMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee_id', 'role')
    fields = ['employee_id','role']

class FlightAdmin(admin.ModelAdmin):
    list_display = ('id', 'flight_number', 'airplane_id', 'departure_day','connection_id')
    fields = ['flight_number',('airplane_id','connection_id'), ('departure_day', 'departure_time'),('arrival_day', 'arrival_time')]

class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticket_number', 'date_time_of_issue', 'price','client_id')
    fields = ['ticket_number', 'date_time_of_issue', 'price']

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'transaction_number', 'id_client', 'ticket_id')
    fields = ['transaction_number', ('id_client', 'ticket_id')]

class AirportAdmin(admin.ModelAdmin):
    list_display = ('id', 'airport_name', 'code', 'country')
    fields = ['airport_name', 'code','country']

class AirplaneAdmin(admin.ModelAdmin):
    list_display = ('id', 'immatriculation', 'type')
    fields = ['immatriculation', 'type']

class DepartureAdmin(admin.ModelAdmin):
    list_display = ('id', 'flight_id', 'pilot_id', 'optional_pilot_id', 'first_crew_member_id', 'second_crew_member_id','number_of_empty_seat','number_of_reserved_seat')
    fields = ['flight_id', ('pilot_id', 'optional_pilot_id'), ('first_crew_member_id','second_crew_member_id'),('number_of_empty_seat','number_of_reserved_seat')]

# Register the admin class with the associated model
admin.site.register(Pilot, PilotAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(CrewMember,CrewMemberAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Departure, DepartureAdmin)
admin.site.register(Airport, AirportAdmin)
admin.site.register(Airplane, AirplaneAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Client, ClientAdmin)

