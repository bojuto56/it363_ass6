from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Album, Photo
from .forms import AlbumForm, PhotoForm

class OwnerOrAdminMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.owner or self.request.user.groups.filter(name="Album Admin").exists()


class AlbumListView(LoginRequiredMixin, ListView):
    model = Album
    template_name = "albums/album_list.html"
    context_object_name = "albums"

    def get_queryset(self):
        if self.request.user.groups.filter(name="Album Admin").exists():
            return Album.objects.all()
        return Album.objects.filter(owner=self.request.user)


class AlbumDetailView(LoginRequiredMixin, DetailView):
    model = Album
    template_name = "albums/album_detail.html"


class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    form_class = AlbumForm
    template_name = "albums/album_form.html"
    success_url = reverse_lazy("album-list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class AlbumUpdateView(LoginRequiredMixin, OwnerOrAdminMixin, UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = "albums/album_form.html"
    success_url = reverse_lazy("album-list")


class AlbumDeleteView(LoginRequiredMixin, OwnerOrAdminMixin, DeleteView):
    model = Album
    template_name = "albums/album_confirm_delete.html"
    success_url = reverse_lazy("album-list")


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = "albums/photo_form.html"
    success_url = reverse_lazy("album-list")