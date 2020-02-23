from django.forms import ModelForm
from .models import Booking
            

class BookingForm(ModelForm):
    class Meta:
        model = Booking 
        fields = ('title', 'description','meeting_date','start_time','end_time','meeting_place',)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'class': 'textarea', 'placeholder': ' brief description about the meeting', 'size': '60'})
        self.fields['meeting_date'].widget.attrs.update({'class': 'date', 'placeholder': ' meeting date', 'size': '40'})
        self.fields['start_time'].widget.attrs.update({'class': 'time', 'placeholder': ' meeting start time', 'size': '40'})
        self.fields['end_time'].widget.attrs.update({'class': 'time', 'placeholder': ' meeting closing time', 'size': '40'})
        self.fields['title'].widget.attrs.update({'class': 'textarea', 'placeholder': ' title of the meeting', 'size': '60'})
        self.fields['meeting_place'].widget.attrs.update({'class': 'textarea', 'placeholder': ' select place of meeting'})
        