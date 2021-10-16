from django.forms import ModelForm, fields
from .models import Poll

# creates a template for a form that contains a field 'question', option_one', two etc. 
# this is used so that you do not need to create a new form every time you change HTML
# built in functionality of the ModelForm django template
class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'option_one', 'option_two', 'option_three']