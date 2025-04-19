from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.conf import settings

class Login(View): 
    def get(self, request):
        contexto = {'mensagens': ''}
        if request.user.is_authenticated:
            return redirect('/veiculo')
        else:
            return render(request, 'autenticacao.html', contexto)
        
    def post(self, request):
        usuario = request.POST.get('nome', None)
        senha = request.POST.get('senha', None)

        print(usuario, senha)

        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/veiculo')
            else:
                return render(request, 'autenticacao.html', {'mensagem': 'Usuário está inativo'})
        else:
            return render(request, 'autenticacao.html', {'mensagem': 'Usuário ou senha inválidos'})

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(settings.LOGIN_URL)
