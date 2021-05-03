from django.http import HttpResponse


class AccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponse('Permission Denied')
        return super().dispatch(request, *args, **kwargs)