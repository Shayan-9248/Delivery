from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from .tasks import (
    get_objects_list_task,
    download_object_task,
    delete_object_task,
)
from .mixins import AccessMixin


class BucketList(AccessMixin, LoginRequiredMixin, View):
    template_name = 'base/bucket_list.html'
    login_url = 'account:sign-in'

    def get(self, request):
        objects = get_objects_list_task()
        return render(request, self.template_name, {'objects': objects})


class DownloadBucket(AccessMixin, LoginRequiredMixin ,View):
    login_url = 'account:sign-in'

    def get(self, request, key):
        download_object_task.delay(key)
        messages.success(request, 'Your demand will be response soon', 'success')
        return redirect(request.META.get('HTTP_REFERER'))


class DeleteBucket(AccessMixin, LoginRequiredMixin ,View):
    login_url = 'account:sign-in'

    def get(self, request, key):
        delete_object_task.delay(key)
        messages.success(request, 'Your demand will be response soon', 'success')
        return redirect(request.META.get('HTTP_REFERER'))


def error_404(request, exception=None):
    return render(request, 'base/404.html')