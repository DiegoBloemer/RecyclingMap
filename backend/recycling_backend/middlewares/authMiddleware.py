from django.shortcuts import redirect
from django.conf import settings

class AuthRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Permitir acesso a LOGIN_URL e REGISTER_URL mesmo sem autenticação
        if not request.user.is_authenticated and request.path not in [settings.LOGIN_URL, settings.REGISTER_URL]:
            return redirect(settings.LOGIN_URL)

        # Redirecionar usuários autenticados que tentarem acessar LOGIN_URL para LOGIN_REDIRECT_URL
        if request.user.is_authenticated and request.path == settings.LOGIN_URL:
            return redirect('/')


        return self.get_response(request)
