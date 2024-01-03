from django.shortcuts import redirect


class LoadLogin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('account_app:login')
        return super().dispatch(request, *args, **kwargs)
