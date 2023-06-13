from django.contrib.auth.models import User
from django.forms import forms
from .models import Visitor, Store, Product, Purchase, Review
from django import forms


class RegistrationForm(forms.Form):
    ROLES = (
        ('buyer', 'Покупатель'),
        ('manager', 'Менеджер'),
    )

    username = forms.CharField(label='Имя пользователя', max_length=100)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    role = forms.ChoiceField(label='Роль', choices=ROLES)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким именем уже существует')
        return username


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ('name', 'email')


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('name', 'location')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'description')


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['visitor', 'store', 'purchase_date', 'amount']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['visitor', 'product', 'rating', 'comment']
        widgets = {
            'visitor': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }
