from django import forms
from app_food.models import Food
from .models import Subscription

class FoodMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.title

class SubscriptionForm(forms.Form):
    name = forms.CharField(max_length=60, required=True, label="Firstname-Lastname")
    email = forms.EmailField(max_length=60, required=True, label="email")
    food_set = FoodMultipleChoiceField(
        queryset=Food.objects.order_by('-is_premium'),
        required=True,
        label="Choose favors:",
        widget=forms.CheckboxSelectMultiple
    )
    accepted = forms.BooleanField(required=True, label="Lorem ipsum dolor sit ametLorem ipsum dolor sit amet")


# ModelClass 
class SubscriptionModelForm(forms.ModelForm):
    food_set = FoodMultipleChoiceField(
        queryset=Food.objects.order_by('-is_premium'),
        required=True,
        label="Choose favors:",
        widget=forms.CheckboxSelectMultiple
    )
    accepted = forms.BooleanField(required=True, label="Lorem ipsum dolor sit ametLorem ipsum dolor sit amet")


    class Meta: # tell how it show and recieve
        model = Subscription # ขอมูลมาจากmodelตัวไหน
        fields = ['name', 'email', 'food_set', 'accepted']
        labels = {
            'name' : 'Firstname-Lastname',
            'email': 'Email',
            'food_set': 'Choose favors',
        }

