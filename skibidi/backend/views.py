from backend.serializers import AnimeSerializer, KindSerializer, WatchingSerializer, KindAnimeSerializer, UserSerializer, EpisodeSerializer, PersonalKindSerializer
from rest_framework import generics
from backend.models import  Anime, Episode, Kind, Watching, KindAnime, PersonalKind
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import WatchingForm, KindForm, AnimeForm, EpisodeForm, KindAnimeForm, PersonalKindForm
from django.urls import reverse
from rest_framework import permissions


def success(request):
    return render(request, 'success.html', {'msg': 'Operazione riuscita!'})

class AnimeListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Anime.objects.order_by('name','season')
    serializer_class = AnimeSerializer

class AnimeUniqueListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Anime.objects.filter(season=1)
    serializer_class = AnimeSerializer

class SeasonsListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    serializer_class = AnimeSerializer
    
    def get_queryset(self):
        return Anime.objects.filter(name=self.kwargs['anime'])

class EpisodesListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    serializer_class = AnimeSerializer
    
    def get_queryset(self):
        return Anime.objects.filter(name=self.kwargs['anime'], season=self.kwargs['season'])
    
class KindListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    serializer_class = KindSerializer
    queryset = Kind.objects.all()

class UserListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class WatchingListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Watching.objects.all()
    serializer_class = WatchingSerializer

class KindAnimeListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = KindAnime.objects.all()
    serializer_class = KindAnimeSerializer

class SpecificAnimeKindListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    serializer_class = KindAnimeSerializer
    
    def get_queryset(self):
        return KindAnime.objects.filter(ka_anime_id=self.kwargs['anime_id'])

class AnimeEpisodeListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    serializer_class = EpisodeSerializer

    def get_queryset(self):
        return Episode.objects.filter(e_anime=self.kwargs['anime_id'])

#---- CreateViews----

class KindCreateView(CreateView): 
    form_class = KindForm
    model = Kind
    template_name="form.html"
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    def get_success_url(self):
        return reverse('success')

class AnimeCreateView(CreateView):
    form_class = AnimeForm
    model = Anime
    template_name = "form.html"
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    def get_success_url(self):
        return reverse('success')

class EpisodeCreateView(CreateView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    form_class = EpisodeForm
    model = Episode
    template_name = "form.html"

    def get_success_url(self):
        return reverse('success')

class UserCreateView(CreateView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    form_class = UserCreationForm
    model = User
    template_name = "form.html"

    def get_success_url(self):
        return reverse('success')

class KindAnimeCreateView(CreateView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    form_class = KindAnimeForm
    model = KindAnime
    template_name = "form.html"

    def get_success_url(self):
        return reverse('success')

class WatchingCreateView(CreateView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    form_class = WatchingForm
    model = Watching
    template_name = "form.html"

    def get_success_url(self):
        return reverse('success')

class PersonalKindCreateView(CreateView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    form_class = PersonalKindForm
    model = PersonalKind
    template_name = "form.html"

    def get_success_url(self):
        return reverse('success')         

#---- UpdateViews----

class EpisodeUpdateView(UpdateView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    form_class = EpisodeForm
    model = Episode
    template_name = "form.html"

    def get_success_url(self):
        return reverse('success')

class AnimeUpdateView(UpdateView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    form_class = AnimeForm
    model = Anime
    template_name = "form.html"

    def get_success_url(self):
        return reverse('success')

class KindUpdateView(UpdateView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    form_class = KindForm
    model = Kind
    template_name = "form.html"

    def get_success_url(self):
        return reverse('success')

class UserUpdateView(UpdateView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    form_class = UserCreationForm
    model = User
    template_name = "form.html"

    def get_success_url(self):
        return reverse('success')

class KindAnimeUpdateView(UpdateView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    form_class = KindAnimeForm
    model = KindAnime
    template_name = "form.html"

    def get_success_url(self):
        return reverse('success')

class WatchingUpdateView(UpdateView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    form_class = WatchingForm
    model = Watching
    template_name = "form.html"

    def get_success_url(self):
        return reverse('success')  

class PersonalKindUpdateView(UpdateView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    form_class = PersonalKindForm
    model = PersonalKind
    template_name = "form.html"

    def get_success_url(self):
        return reverse('success') 

#---- DeleteViews----

class KindDeleteView(DeleteView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    model = Kind
    template_name = "confirm_delete.html"

    def get_success_url(self):
        return reverse('success')

class AnimeDeleteView(DeleteView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    model = Anime
    template_name = "confirm_delete.html"

    def get_success_url(self):
        return reverse('success')

class EpisodeDeleteView(DeleteView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    model = Episode
    template_name = "confirm_delete.html"

    def get_success_url(self):
        return reverse('success')

class UserDeleteView(DeleteView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    model = User
    template_name = "confirm_delete.html"

    def get_success_url(self):
        return reverse('success')

class KindAnimeDeleteView(DeleteView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    model = KindAnime
    template_name = "confirm_delete.html"

    def get_success_url(self):
        return reverse('success')

class WatchingDeleteView(DeleteView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    model = Watching
    template_name = "confirm_delete.html"

    def get_success_url(self):
        return reverse('success')  

class PersonalKindDeleteView(DeleteView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    model = PersonalKind
    template_name = "confirm_delete.html"

    def get_success_url(self):
        return reverse('success')  

def add_personal(request, user, kind):
    p_user = User.objects.get(username=user)
    p_kind = Kind.objects.get(kind_name=kind)
    p = PersonalKind(p_user=p_user, p_kind=p_kind)
    p.save()
    return redirect('/profile/')

def del_personal(request, user, kind):
    p_user = User.objects.get(username=user)
    p_kind = Kind.objects.get(kind_name=kind)
    PersonalKind.objects.filter(p_user=p_user, p_kind=p_kind).delete()
    return redirect('/profile/')