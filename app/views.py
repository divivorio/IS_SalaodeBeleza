from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import User, List, Item, Especialidade, Prestador, Cliente, Agenda, Atendimento
from .forms import PrestadorForm, ClienteForm, EspForm, AgendaForm, AtendimentoForm

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render (request, 'app/app.html')
    else:
        return redirect('page_login')

def page_login(request):
    return render(request, 'app/login.html',{})
def pagina_inicial(request):
    return render(request, 'app/index.html', {})
def autenticar_usuario(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        prestadores = Prestador.objects.all()
        return render(request, 'app/listar_prestadores.html', {'prestadores':prestadores})
    else:
        return render(request, 'app/login.html',{})

def app_logout(request):
    logout(request)
    return redirect('page_login')

def todo_list(request, list_id):
    #list = List.objects.get(pk=list_id)
    list = get_object_or_404(List, pk=list_id, user=request.user)
    return render(request, 'app/list.html', context={
        'list': list
    })

def add_item(request, list_id):
    item_title = request.POST.get('item_title')
    list = get_object_or_404(List, pk=list_id, user=request.user)
    item = Item(title=item_title, list=list)
    item.save() # será salvo na base de dados
    return redirect('todo_list', list_id=list_id)

def remove_item(request, list_id, item_id):
    list = get_object_or_404(List, pk=list_id, user=request.user)
    item = get_object_or_404(Item, pk=item_id, list=list)
    item.delete()
    return redirect('todo_list', list_id=list_id)

def done_item(request, list_id, item_id):
    list = get_object_or_404(List, pk=list_id, user=request.user)
    item = get_object_or_404(Item, pk=item_id, list=list)
    item.done = not item.done
    item.save()
    return redirect('todo_list', list_id=list_id)
# especialidade

def listar_especialidades(request):
    especialidades = Especialidade.objects.all()
    return render(request, 'app/listar_especialidades.html', {'especialidades':especialidades})

def cadastrar_especialidade(request):
    if request.method == "POST":
        form = EspForm(request.POST, request.FILES)
        if form.is_valid():
            especialidade = form.save(commit=False)
            form.save()
            return redirect('listar_especialidades')
    else:
        form = EspForm()
    return render(request, 'app/editar_especialidade.html', {'form': form})


def listar_prestadores(request):
    prestadores = Prestador.objects.all()
    return render(request, 'app/listar_prestadores.html', {'prestadores':prestadores})

def detalhar_prestador(request, id):
    prestador = get_object_or_404(Prestador, pk=id)
    return render(request, 'app/detalhar_prestador.html', {'prestador':prestador})

def cadastrar_prestador(request):
    if request.method == "POST":
        form = PrestadorForm(request.POST, request.FILES)
        if form.is_valid():
            prestador = form.save(commit=False)
            form.save()
            return redirect('detalhar_prestador', id=prestador.id)
    else:
        form = PrestadorForm()
    return render(request, 'app/editar_prestador.html', {'form': form})


def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'app/listar_clientes.html', {'clientes':clientes})

def detalhar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    return render(request, 'app/detalhar_cliente.html', {'cliente':cliente})

def cadastrar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            cliente = form.save(commit=False)
            form.save()
            return redirect('detalhar_cliente', id=cliente.id)
    else:
        form = ClienteForm()
    return render(request, 'app/editar_cliente.html', {'form': form})


def listar_agenda(request):
    agendas = Agenda.objects.all()
    atendimentos = Atendimento.objects.all()
    return render(request, 'app/listar_agenda.html', {'agendas': agendas, 'atendimentos': atendimentos})

def cadastrar_agenda(request):
    if request.method == "POST":
        form = AgendaForm(request.POST, request.FILES)
        if form.is_valid():
            agenda = form.save(commit=False)
            form.save()
            return redirect('listar_agenda')
    else:
        form = AgendaForm()
    return render(request, 'app/editar_agenda.html', {'form': form})

def cadastrar_atendimento(request):
    if request.method == "POST":
        form = AtendimentoForm(request.POST, request.FILES)
        if form.is_valid():
            atendimento = form.save(commit=False)
            form.save()
            return redirect('pagina_inicial')
    else:
        form = AtendimentoForm()
    return render(request, 'app/editar_atendimento.html', {'form': form})
