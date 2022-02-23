from django.views.generic import CreateView,UpdateView
from django.shortcuts import get_object_or_404
from editais.forms.form_pergunta import PerguntaForm, Formset_PergAlter
from django.shortcuts import redirect,render
from editais.models import Edital,Pergunta


def pergunta_add(request, id):
   
    edital = get_object_or_404(Edital, pk=id)
    pergunta = Pergunta()
    pergunta.edital = edital
    context = {}

    if request.method == 'POST':

        form = PerguntaForm(request.POST or None, request.FILES or None, instance=pergunta, prefix='pergunta')
        formset = Formset_PergAlter(request.POST or None, request.FILES or None, instance=pergunta,
                                                    prefix='alternativa')

        if form.is_valid() and formset.is_valid():
            form = form.save(commit=False)
            form.save()
            formset.save()
            return redirect('editais:edital_detalhe', id=edital.id)
        else:
            context['edital'] = edital
            context['form'] = PerguntaForm(request.POST or None, request.FILES or None, instance=pergunta,
                                           prefix='pergunta')
            context['formset'] = Formset_PergAlter(request.POST or None, request.FILES or None,
                                                                   instance=pergunta, prefix='alternativa')


    context['edital'] = edital
    context['form'] = PerguntaForm(instance=pergunta, prefix='pergunta')
    context['formset'] = Formset_PergAlter( instance=pergunta, prefix='alternativa')

    return render(request, 'pergunta/form_pergunta.html', context)



def editar_pergunta(request,id):

    pergunta = get_object_or_404(Pergunta, pk=id)
    edital = pergunta.edital
    context = {}

    
    if request.method == 'POST':
    
        form = PerguntaForm(request.POST or None, request.FILES or None, instance=pergunta, prefix='pergunta')
        formset = Formset_PergAlter(request.POST or None, request.FILES or None, instance=pergunta, prefix='alternativa')

        if form.is_valid() and formset.is_valid():
            form = form.save(commit=False)
            form.save()
            formset.save()
            return redirect('editais:edital_view', id=edital.id)
        else:
            context['edital'] = edital
            context['form'] = PerguntaForm(request.POST or None, request.FILES or None, instance=pergunta,
                                           prefix='pergunta')
            context['formset'] = Formset_PergAlter(request.POST or None, request.FILES or None,
                                                                   instance=pergunta, prefix='alternativa')

    context['edital'] = edital
    context['form'] = PerguntaForm(instance=pergunta, prefix='pergunta')
    context['formset'] = Formset_PergAlter( instance=pergunta, prefix='alternativa')

    return render(request, 'pergunta/form_pergunta.html', context)
