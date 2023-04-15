from django.db.models import Model, ForeignKey, CASCADE, DateTimeField


class Attandance(Model):
    employee = ForeignKey('employee.Employee', CASCADE, 'attandanes')
    start_work = DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'attandance'

    def __str__(self):
        return str(self.start_work.strftime("%H:%M:%S"))
