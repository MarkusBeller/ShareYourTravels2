from django import forms

from Photogallery.models import Item


from django import forms
from django.forms import ModelForm





class UploadFileForm(ModelForm):
    class Meta:
        model =Item
        fields = ['name', 'description', 'image', 'category']

form = UploadFileForm()





#TestKlasse funktioniert nicht wegen ForeignKey

#class UploadFileForm(forms.Form):

#    description = forms.CharField()
#    image = forms.ImageField()
#    category = forms.ModelChoiceField





