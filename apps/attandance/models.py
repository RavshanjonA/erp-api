from django.db.models import Model, ForeignKey, CASCADE, DateTimeField


class Attandance(Model):
    user = ForeignKey('employee.Employee', CASCADE, 'attandanes')
    start_work = DateTimeField()
