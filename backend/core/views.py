from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import LocalReciclagem, Imagem
from .forms import LocalReciclagemForm, ImagemForm
from django.shortcuts import get_object_or_404
from .models import TipoResiduo

# Create your views here.


def home(request):
    tipos_residuos = TipoResiduo.objects.all()
    return render(request, 'home.html', {'tipos_residuos': tipos_residuos})

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')


# Função para adicionar um local de reciclagem
def adicionar_local(request):
    if request.method == 'POST':
        # Buscar o tipo de resíduo pelo ID ou criar um erro caso não exista
        tipo_residuo_id = request.POST.get('tipo_residuo')
        tipo_residuo = get_object_or_404(TipoResiduo, id=tipo_residuo_id)

        # Criar um formulário com base nos dados enviados
        local_form = LocalReciclagemForm({
            'nome': request.POST.get('nome'),
            'latitude': request.POST.get('latitude'),
            'longitude': request.POST.get('longitude'),
            'endereco': request.POST.get('endereco'),
            'tipo_residuo': tipo_residuo.id,
        })

        imagens = request.FILES.getlist('imagens')  # Receber arquivos de imagem
        
        if local_form.is_valid():
            local = local_form.save(commit=False)
            local.tipo_residuo = tipo_residuo  # Associar o tipo de resíduo
            local.save()  # Salvar o local

            # Salvar imagens associadas ao local
            for imagem in imagens:
                img_obj = Imagem.objects.create(imagem=imagem)
                local.imagens.add(img_obj)  # Vincular a imagem ao local
            
            return redirect('home')  # Redireciona após sucesso
        else:
            return HttpResponse("Erro no formulário.", status=400)

    return render(request, 'adicionar_local.html')
