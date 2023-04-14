from django.db.models import Model, ForeignKey, CASCADE, DateTimeField


class Attandance(Model):
    employee = ForeignKey('employee.Employee', CASCADE, 'attandanes')
    start_work = DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'attandance'
