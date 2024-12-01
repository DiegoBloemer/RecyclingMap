from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import LocalReciclagem, Imagem, TipoResiduo
from django.contrib.auth.models import User
from .forms import LocalReciclagemForm, ImagemForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

# Função para renderizar a página inicial
def home(request):
    tipos_residuos = TipoResiduo.objects.all()
    return render(request, 'home.html', {'tipos_residuos': tipos_residuos})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']  # Captura o e-mail inserido
        password = request.POST['password']  # Captura a senha inserida
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Substitua 'home' pela página inicial após o login
        else:
            messages.error(request, "E-mail ou senha inválidos.")  # Exibe mensagem de erro
    return render(request, 'login.html')  # Renderiza o template de login

def register_view(request):
    return render(request, 'register.html')

# Função para logout do usuário

def logout_view(request):
    logout(request)
    return redirect('login')  # Redireciona para a página de login


# Função para adicionar um local de reciclagem
def adicionar_local(request):
    if request.method == 'POST':
        # Buscar o tipo de resíduo pelo ID ou criar um erro caso não exista
        tipo_residuo_id = request.POST.get('tipo_residuo')
        tipo_residuo = get_object_or_404(TipoResiduo, id=tipo_residuo_id)

        # Criar um formulário com base nos dados enviados
        local_form = LocalReciclagemForm({
            'nome': request.POST.get('name'),
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
                local.imagens.add(img_obj)
            local.save()  # Salve a associação ManyToManyField após adicionar imagens     
            messages.success(request, "Local de reciclagem adicionado com sucesso!")
            return redirect('home')  # Redireciona após sucesso
        else:
            return HttpResponse("Erro no formulário.", status=400)

    return render(request, 'adicionar_local.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Verificar se o usuário já existe
            if User.objects.filter(email=email).exists():
                messages.error(request, "Esse e-mail já está cadastrado.")
            else:
                # Criar o usuário
                User.objects.create_user(username=email, email=email, password=password)
                messages.success(request, "Usuário registrado com sucesso!")
                return redirect('login')  # Redirecionar para a página de login
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

# Função para inicializar os marcadores já adicionados (locais de reciclagem)

from django.http import JsonResponse

def pontos_coleta(request):
    locais = LocalReciclagem.objects.prefetch_related('imagens').all()
    dados = []
    for local in locais:
        imagens_urls = [imagem.imagem.url for imagem in local.imagens.all()]
        dados.append({
            'nome': local.nome,
            'endereco': local.endereco,
            'latitude': local.latitude,
            'longitude': local.longitude,
            'tipo_residuo': local.tipo_residuo.nome,  # Ajuste se necessário
            'imagens': imagens_urls,
        })
    return JsonResponse(dados, safe=False)

# Função para buscar os pontos pelos filtros de tipo de resíduo e endereço

def buscar_pontos(request):
    termo_busca = request.GET.get('search', '')  # Captura o termo de busca da URL
    pontos = LocalReciclagem.objects.filter(
        Q(endereco__icontains=termo_busca) | Q(tipo_residuo__nome__icontains=termo_busca)
    ).prefetch_related('imagens')

    resultados = []
    for ponto in pontos:
        imagens_urls = [request.build_absolute_uri(imagem.imagem.url) for imagem in ponto.imagens.all()]
        resultados.append({
            'nome': ponto.nome,
            'endereco': ponto.endereco,
            'latitude': ponto.latitude,
            'longitude': ponto.longitude,
            'tipo_residuo': ponto.tipo_residuo.nome,
            'imagens': imagens_urls,
        })

    return JsonResponse(resultados, safe=False)

