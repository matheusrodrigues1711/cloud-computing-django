from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm


def lista_produtos(request):
    produtos = Produto.objects.all()

    return render(request, 'produtos/lista.html', {
        'produtos': produtos
    })


def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()

    return render(request, 'produtos/formulario.html', {
        'form': form
    })


def editar_produto(request, id):
    produto = Produto.objects.get(id=id)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)

        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'produtos/formulario.html', {
        'form': form,
        'editar': True
    })


def excluir_produto(request, id):
    produto = Produto.objects.get(id=id)

    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')

    return render(request, 'produtos/confirmar_exclusao.html', {
        'produto': produto
    })