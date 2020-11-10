from django.shortcuts import render
from django.views import generic
from .forms import PackForm, PackComponentsForm, PackComponentsFormSet
from .models import Pack, Component, PackComponent


def adding_pack_view(request):
    if request.method == 'POST':
        # print(request.POST)
        # print(request.POST['name'])
        pack_form = PackForm(request.POST)
        component_formset = PackComponentsFormSet(request.POST)
        # print(pack_form)
        # print(component_formset)
        if pack_form.is_valid() and component_formset.is_valid():
            pack = pack_form.save()

            for component_form in component_formset:
                component_data = component_form.cleaned_data
                if component_data:
                    component = Component.objects.get_or_create(
                        component_name=component_data['component_name']
                    )
                    pack_component = PackComponent.objects.create(
                        component=component[0], 
                        pack=pack,
                        amount=component_data['amount']
                    )
    else:
        pack_form = PackForm()
        component_formset = PackComponentsFormSet()

    context = {
        'pack_form': pack_form,
        'component_formset': component_formset,
    }
    
    return render(request, 'adding_pack.html', context)



class ShowPackDetails(generic.DetailView):
    template_name = 'pack_details.html'
    model = Pack
    context_object_name = 'pack'

    def get_context_data(self, **kwargs):
        try:
            context = super(ShowPackDetails, self).get_context_data(**kwargs)
            context['components'] = PackComponent.objects.filter(pack=self.get_object())
        except:
            return context
        return context