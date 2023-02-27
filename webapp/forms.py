from django import forms
from django.core.exceptions import ValidationError
from webapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = {'title', 'description', 'category', 'photo', 'count', 'price'}
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'category': 'Категория',
            'photo': 'Фото',
            'count': 'Остаток',
            'price': 'Цена'
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise ValidationError('Заголовок должен быть длиннее 2 символов!')
        return title
