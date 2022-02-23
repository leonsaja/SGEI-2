from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from editais.forms import form_edital
from editais.models import Edital


class CriarEdital(SuccessMessageMixin, CreateView):
    form_class = form_edital.CriarEditalForm
    template_name = 'edital/edital_form.html'
    success_url = reverse_lazy('edital:listar_editais')


class EditarEdital(SuccessMessageMixin, UpdateView):
    model = Edital
    form_class = form_edital.EditarEditalForm
    template_name = 'edital/edital_form.html'
    success_url = reverse_lazy('edital:listar_editais')
    success_message = 'Edital atualizado com sucesso'


class ListarEdital(ListView):

    model = Edital
    context_object_name = 'editais'
    template_name = 'edital/listar_editais.html'
    paginate_by = 25

    def get_queryset(self):
        return Edital.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListarEdital, self).get_context_data(**kwargs)
        context['quant_pages'] = ['10', '15', '25', '35', '50']
        context['limit_page'] = self.paginate_by
        return context


class RemoverEdital(SuccessMessageMixin, DeleteView):
    model = Edital
    template_name = 'edital/edital_confirm_delete.html'
    success_url = reverse_lazy('edital:listar_editais')
    success_message = 'Edital excluído com sucesso'


def edital_view_adm(request, id):
    context = {}
    edital = get_object_or_404(Edital, pk=id)
    print('teste')
    perguntas = edital.pergunta_set.all()
    context['edital'] = edital
    context['perguntas'] = perguntas
    return render(request, 'edital/edital_detail.html', context)


# class DetalheEditalView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
#     model = Edital
#     template_name = 'edital/edital_detail.html'
#
#     def get_context_data(self, **kwargs):
#         context=super(DetalheEditalView, self).get_context_data(**kwargs)
#         context['edital'] =Edital.objects.get(pk=self.kwargs['pk'])
#         context['perguntas']=context['edital'].pergunta_set.all()
#
#         return context
