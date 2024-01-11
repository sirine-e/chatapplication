from django import forms
from .models import Room

class RoomCreationForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'slug']

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if Room.objects.filter(slug=slug).exists():
            raise forms.ValidationError('This slug is already in use.')
        return slug