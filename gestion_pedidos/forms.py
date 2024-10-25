from django import forms


# Por cada formulario se debe crear una clase
class FormularioContacto(forms.Form):
    asunto = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)
