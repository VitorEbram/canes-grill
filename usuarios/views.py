from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

from churras.models import Prato

def cadastro(request):
    #print(f'Method: {request.method}')
    if request.method == "POST":
        
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']
        
        if not nome.strip():
            print("O campo nome não pode ficar em branco")
            return redirect("cadastro")
        
        if not email.strip():
            print("O campo email não pode ficar em branco")
            return redirect("cadastro")

        if senha != senha2 or not senha.strip() or not senha2.strip():
            print("Senhas em branco ou diferentes")
            return redirect("cadastro")
            
        if User.objects.filter(email=email).exists():
            print("Email já cadastrado")
            return redirect("cadastro")
        
        if User.objects.filter(username=nome).exists():
            print("Usuário já cadastrado")
            return redirect("cadastro")
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print("Usuário cadastrado com sucesso")
        return redirect("login")
                
    return render(request, 'cadastro.html')


def login(request):
    if request.method == "POST":
        
        email = request.POST['email'].strip()
        senha = request.POST['senha'].strip()
        
        if email == "" or senha == "":
            print("Os campos email e senha não podem ficar em branco")
            return redirect("login")
        
        if User.objects.filter(email=email).exists:
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            
            if user is not None:
                auth.login(request, user)
                print("Login realizado com sucesso.")
                return render(request, 'dashboard.html')
        
        print("Usuário e/ou senha inválidas")
        return redirect("dashboard") 
        
    return render(request, 'login.html')


def dashboard(request):
    if request.user.is_authenticated:
        pratos = Prato.objects.filter(publicado=True).order_by('-date_prato')
        
    
        contexto = {
            'lista_pratos' : pratos,
        }
        return render(request, "dashboard.html", contexto)
 
    return redirect('index')

def logout(request):
    auth.logout(request)
    print("Você realizou o logout")
    return redirect("index")

def cria_prato(request):
    if request.method =='POST':
        # recuperar dados do formulário
        print(f'\n{request.POST["nome_prato"]}')
        nome_prato = request.POST['nome_prato']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_prato = request.FILES['foto_prato']

        prato = Prato.objects.create_prato()
    
    
    return render(request, 'cria_prato.html')

