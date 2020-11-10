from django import forms
from .models import Pack, Component


class PackForm(forms.ModelForm):
    pack_name = forms.CharField(max_length=100, label="Pack name")
    class Meta:
        model = Pack
        fields = ['pack_name']

    # def save(self, commit=True):
    #     instance = super(PackForm, self).save(commit=False)
    #     try:
    #         pack = Pack.objects.get(pack_name=instance.pack_name)
    #     except:
    #         pack = None
    #     if commit and not pack:
    #         Pack.objects.create(pack_name=instance.pack_name)
    #     return pack


# class ComponentForm(forms.ModelForm):
#     component_name = forms.CharField(max_length=100, label="Component name")
#     class Meta:
#         model = Component
#         fields = ['component_name']


class PackComponentsForm(forms.Form):
    component_name = forms.CharField(max_length=100, label="Component name")
    amount = forms.IntegerField()

    class Meta:
        fields = ['amount']


PackComponentsFormSet = forms.formset_factory(
    PackComponentsForm,
    extra=3,
    min_num=1,
    max_num=5,
    validate_max=True,
    validate_min=True
)