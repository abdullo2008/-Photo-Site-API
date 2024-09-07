from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ViewSet, ModelViewSet, ReadOnlyModelViewSet

from .forms import PhotoModelForm
from .models import PhotoModel
from .serializers import PhotoSerializer
from django.views.generic import CreateView, DeleteView, UpdateView


# API Views
class CreateAPIPhoto(ListCreateAPIView):
    queryset = PhotoModel.objects.all()
    serializer_class = PhotoSerializer


class UpdateDeletePhotoAPIView(RetrieveUpdateDestroyAPIView):
    queryset = PhotoModel.objects.all()
    serializer_class = PhotoSerializer


class PhotoViewSet(ReadOnlyModelViewSet):
    queryset = PhotoModel.objects.all()
    serializer_class = PhotoSerializer


# Site Views
def ListPhoto(request):
    model = PhotoModel.objects.all()
    context = {
        'photos': model
    }
    return render(request, 'index.html', context)


class CreatePhoto(CreateView):
    model = PhotoModel
    template_name = 'addphoto.html'
    fields = ['title', 'photo', 'caption']
    success_url = reverse_lazy('index')


class DeletePhoto(DeleteView):
    model = PhotoModel
    template_name = 'delete.html'
    success_url = reverse_lazy('index')


class UpdatePhoto(UpdateView):
    model = PhotoModel
    template_name = 'update.html'
    form_class = PhotoModelForm
    success_url = reverse_lazy('index')


def about(request):
    return render(request, 'about.html')
