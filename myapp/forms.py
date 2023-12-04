# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Dataset, Visualization

class CustomAuthenticationForm(AuthenticationForm):
    # Add any customizations to the authentication form if needed
    pass

class CustomUserCreationForm(UserCreationForm):
    # Add any customizations to the user creation form if needed
    pass

class DatasetUploadForm(forms.ModelForm):
    class Meta:
        model = Dataset
        fields = ['name', 'file']

class VisualizationForm(forms.ModelForm):
    class Meta:
        model = Visualization
        fields = ['name', 'description']

class DataColumnForm(forms.Form):
    column_name = forms.CharField(max_length=255)
    data_type = forms.CharField(max_length=50)

class DataPointForm(forms.Form):
    # Update the DataPointForm fields based on your dynamic columns
    pass
