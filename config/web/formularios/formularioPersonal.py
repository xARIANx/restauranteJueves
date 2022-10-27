#los formularios de Django son clases

from django import forms


class FormularioPersonal(forms.Form):

    #creando atributo para cargar el selector
    OPCIONES=(
        (1,'Administrador'),
        (2,'Chef'),
        (3,'Meseros'),
        (4,'Aseo')
    )

    #creando atributos para sexo 
    OPCIONES2=(
        (1,'Hombre'),
        (2,'Mujer')
    )

    #Dentro de la clase cada atributo sera un input

    nombrePersona=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True,
        max_length=10
    )

    idPersona=forms.CharField(
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'}),
        required=True,
        max_length=11
    )

    edadPersona=forms.CharField(
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'}),
        required=True,
        max_length=2
    )

    sexoPersona=forms.ChoiceField(
        widget=forms.Select(attrs={'class':'form-control mb-3'}),
        required=True,
        choices=OPCIONES2
    )

    tipoPersonal=forms.ChoiceField(
        widget=forms.Select(attrs={'class':'form-control mb-3'}),
        required=True,
        choices=OPCIONES
    )