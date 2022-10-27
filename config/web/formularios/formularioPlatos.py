#los formularios de Django son clases

from django import forms


class FormularioPlatos(forms.Form):

    #creando atributo para cargar el selector
    OPCIONES=(
        (1,'Entrada'),
        (2,'Plato fuerte'),
        (3,'Postre')
    )

    #Dentro de la clase cada atributo sera un input

    nombrePlato=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True,
        max_length=5
    )

    descripcionPlato=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=False,
        max_length=20
    )

    fotoPlato=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True
    )

    precioPlato=forms.CharField(
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'}),
        required=True
    )

    tipoPlato=forms.ChoiceField(
        widget=forms.Select(attrs={'class':'form-control mb-3'}),
        required=True,
        choices=OPCIONES
    )