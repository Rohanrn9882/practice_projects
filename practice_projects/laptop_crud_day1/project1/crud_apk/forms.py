from tkinter import Widget
from django import forms
from .models import Laptop

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'

        labels={
            'laptop_id' : 'LAPTOP_ID',
            'name' : 'NAME',
            'brand' : 'BRAND',
            'ram' : 'RAM',
            'rom' : 'ROM',
            'hdd' : 'HDD',
            'ssd' : 'SSD',
            'price' : 'PRICE'
        }

        widgets= {
            'laptop_id' : forms.NumberInput(attrs={
                'placeholder' : 'eg.1',
                'autocomplete' : 'off'
            }),

            'name' : forms.TextInput(attrs={
                'placeholder' : 'enter laptop name',
                'autocomplete' : 'off',
            }),

            'brand' : forms.TextInput(attrs={
                'placeholder' : 'enter brand name',
                'autocomplete' : 'off'
            }),

            'ram' : forms.TextInput(attrs={
                'placeholder' : 'enter laptop ram',
                'autocomplete' : 'off'
            }),

            'rom' : forms.TextInput(attrs={
                'placeholder' : 'enter laptop rom ',
                'autocomplete' : 'off'
            }),

            'hdd' : forms.TextInput(attrs={
                'placeholder' : 'enter hdd details in gb',
                'autocomplete' : 'off'
            }),

            'ssd' : forms.TextInput(attrs={
                'placeholder' : 'enter ssd details in gb',
                'autocomplete' : 'off'
            }),

            'price' : forms.NumberInput(attrs={
                'placeholder' : 'eg.12345',
                'autocomplete' : 'off'
            })


        }

