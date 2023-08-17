from django import forms

from .models import Appointment
from tasks.models import Task


class BookingForm(forms.ModelForm):
    """
    This is a custom form used to create and update Appointment instances
    """
    class Meta:
        model = Appointment
        fields = [
            "appointment_day",
            "appointment_start_time",
            "appointment_end_time",
            "appointment_tasks",
        ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields["appointment_tasks"].queryset = Task.objects.filter(
            owner=self.request.user
        ).filter(done=False).filter(due_date=None)
        field = self.fields["appointment_day"]
        field.widget = field.hidden_widget()
    appointment_tasks = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Task.objects.all(),
    )
