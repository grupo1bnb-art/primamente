from django import forms
from .models import Producto, CuentaBancaria


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'ingreso_diario', 'limite', 'duracion', 'imagen', 'activo']


class CuentaBancariaForm(forms.ModelForm):
    class Meta:
        model = CuentaBancaria
        fields = ['banco', 'destinatario', 'numero_cuenta', 'activa']
        widgets = {
            'banco': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: BAC, Banpro, Binance'
            }),
            'destinatario': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del titular'
            }),
            'numero_cuenta': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de cuenta o wallet'
            }),
            'activa': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }