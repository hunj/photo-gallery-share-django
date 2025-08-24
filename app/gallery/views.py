from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Album, Photo
from .forms import AlbumForm, PhotoForm


class AlbumListView(ListView):
    model = Album
    template_name = 'gallery/album_list.html'
    context_object_name = 'albums'
    paginate_by = 12
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            # Show user's albums and public albums
            return Album.objects.filter(
                Q(owner=self.request.user) | Q(is_public=True)
            ).select_related('owner')
        else:
            # Show only public albums
            return Album.objects.filter(is_public=True).select_related('owner')


class AlbumDetailView(DetailView):
    model = Album
    template_name = 'gallery/album_detail.html'
    context_object_name = 'album'
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            # Show user's albums and public albums
            return Album.objects.filter(
                Q(owner=self.request.user) | Q(is_public=True)
            ).select_related('owner')
        else:
            # Show only public albums
            return Album.objects.filter(is_public=True).select_related('owner')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = self.object.photos.all()
        return context


class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'gallery/album_form.html'
    success_url = reverse_lazy('gallery:album_list')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, 'Album created successfully!')
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class AlbumUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'gallery/album_form.html'
    
    def test_func(self):
        album = self.get_object()
        return album.owner == self.request.user or self.request.user.is_superuser
    
    def form_valid(self, form):
        messages.success(self.request, 'Album updated successfully!')
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class AlbumDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Album
    template_name = 'gallery/album_confirm_delete.html'
    success_url = reverse_lazy('gallery:album_list')
    
    def test_func(self):
        album = self.get_object()
        return album.owner == self.request.user or self.request.user.is_superuser
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Album deleted successfully!')
        return super().delete(request, *args, **kwargs)


class PhotoListView(ListView):
    model = Photo
    template_name = 'gallery/photo_list.html'
    context_object_name = 'photos'
    paginate_by = 20
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            # Show user's photos and public photos
            return Photo.objects.filter(
                Q(owner=self.request.user) | Q(is_public=True)
            ).select_related('owner', 'album')
        else:
            # Show only public photos
            return Photo.objects.filter(is_public=True).select_related('owner', 'album')


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'gallery/photo_detail.html'
    context_object_name = 'photo'
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            # Show user's photos and public photos
            return Photo.objects.filter(
                Q(owner=self.request.user) | Q(is_public=True)
            ).select_related('owner', 'album')
        else:
            # Show only public photos
            return Photo.objects.filter(is_public=True).select_related('owner', 'album')


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'gallery/photo_form.html'
    success_url = reverse_lazy('gallery:photo_list')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, 'Photo uploaded successfully!')
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class PhotoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'gallery/photo_form.html'
    
    def test_func(self):
        photo = self.get_object()
        return photo.owner == self.request.user or self.request.user.is_superuser
    
    def form_valid(self, form):
        messages.success(self.request, 'Photo updated successfully!')
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class PhotoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Photo
    template_name = 'gallery/photo_confirm_delete.html'
    success_url = reverse_lazy('gallery:photo_list')
    
    def test_func(self):
        photo = self.get_object()
        return photo.owner == self.request.user or self.request.user.is_superuser
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Photo deleted successfully!')
        return super().delete(request, *args, **kwargs)


@login_required
def dashboard(request):
    """User dashboard showing their albums and photos"""
    user_albums = Album.objects.filter(owner=request.user).prefetch_related('photos')
    user_photos = Photo.objects.filter(owner=request.user).select_related('album')
    
    context = {
        'albums': user_albums,
        'photos': user_photos,
        'album_count': user_albums.count(),
        'photo_count': user_photos.count(),
    }
    return render(request, 'gallery/dashboard.html', context)
