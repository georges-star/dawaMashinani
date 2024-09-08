from django.shortcuts import redirect

class CheckLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.session.get('logged_out', False):
            if not request.user.is_authenticated:
                del request.session['logged_out']
                if not request.path.startswith('/accounts/'):  # Exclude URLs related to login/logout
                    return redirect('login')
        return response


