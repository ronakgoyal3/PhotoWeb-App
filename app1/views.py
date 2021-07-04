# from django.shortcuts import render
#
# # Create your views here.
# from django.http import Http404
# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
# from django.template import loader
# from . models import Album Photo
#
# def index(request):
#     all_albums= Album.objects.all()
#     template= loader.get_template('app1/index.html')
#     context={
#         'all_albums':all_albums,
#     }
#     return HttpResponse(template.render(context,request))
# def details(request,album_id):
#     album=get_object_or_404(Album,pk=album_id)
#     return render(request,'app1/details.html',{'album':album})
#
# def favourite(request, album_id):
#     album=get_object_or_404(Album,pk=album_id)
#     try:
#         selected_song=album.song_set.get(pk=request.POST['Photo'])
#     except(KeyError, Photo.DoesNotExist):
#         return render(request, 'app1/details.html',{
#             'album':album,
#             'error_message':"no Photo available bro",
#         })
#     else:
#         selected_song.is_favourite=True
#         selected_song.save()
#         return render(request,'app1/details.html',{'album':album})


from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
from django.views.generic import View
# from .form import UserForm
from .forms import UserRegisterForm
from .models import Album, Photo
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


class IndexView(generic.ListView):
    template_name = 'app1/index.html'
    context_object_name = 'all_albums'
    def get_queryset(self):
        return Album.objects.all()

class Favview(generic.ListView):
    template_name = 'app1/favs.html'
    context_object_name = 'all_albums'
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'app1/details.html'
    
class AlbumCreate(CreateView):
    model = Album
    fields = ['albumtitle','Album_logo']

    def form_valid(self, form):
        form.instance.Owner= self.request.user
        return super().form_valid(form)


# def addphoto(album.id):
#     currentalbum=get_object('Album',pk=album.id)
#     # Album.objects.get(pk=a)
#     photo- picture,albumname
#     albumname=currentalbum.albumtitle
#
#     model = Album
#     fields = ['Picture','albumname']



class PhotoCreate(CreateView):
    model = Photo
    fields = ['Picture','albumname']


    # def form_valid(self, form):
    #     form.instance.albumname= self.request.albumtitle
    #     return super().form_valid(form)

def favourite(request, album_id):
    album= get_object_or_404(Album,pk= album_id)
    try:
        selected_photo=album.photo_set.get(pk=request.POST['photo'])
    except(KeyError, Photo.DoesNotExist):
        return render(request, 'app1/details.html', {
             'album':album,
             'error_message':"no Photo available bro",
        })
    else:
        if(selected_photo.is_favourite):
            selected_photo.is_favourite = False
        else: selected_photo.is_favourite = True
        selected_photo.save()
        return render(request, 'app1/details.html', {'album': album})


def favinfavpage(request, album_id):
    album= get_object_or_404(Album,pk= album_id)
    selected_photo = album.photo_set.get(pk=request.POST['photo'])
    selected_photo.is_favourite = False
    selected_photo.save()
    return redirect('app1:favs')


def PhotoDelete(request,album_id):
    album = get_object_or_404(Album, pk=album_id)
    selected_photo = album.photo_set.get(pk=request.POST['photo_id'])
    selected_photo.delete()
    return render(request, 'app1/details.html', {'album': album})



class AlbumUpdate(UpdateView):
    model = Album
    fields = ['albumtitle','Owner','Album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('app1:index')

    

def register(request):
    if request.method =="POST":
       form = UserRegisterForm(request.POST)
       if form.is_valid():
           form.save()    # save the user in backhand table
           username= form.cleaned_data.get('username')        # .cleaned_data put all data put in forms in dictionary
           messages.success(request, 'Your account has been  created , you are now able to log in')  # messages are diffrent types like success, danger ,ingo etc,...
           return redirect('app1:login')    # takes name which page you want to redirect+
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

# class UserFormView(View):
#     form_class= UserForm
#     template_name='app1/registration_form.html'

#     #display blank form
#     def get(self, request):
#         form= self.form_class(None)
#         return render(request, self.template_name,{'form':form})

#     #process form data
#     def post(self, request):
#         form=self.form_class(request.POST)
#         if form.is_valid():
#             user=form.save(commit=False)
#             #cleaning the data
#             username= form.cleaned_data['username']
#             password=form.cleaned_data['password']
#             user.set_password(password)
#             user.save()

#             #return user ovjects if credentioals are correct
#             user=authenticate(username=username, password=password)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('app1:index')

#         return render(request, self.template_name, {'form':form})
