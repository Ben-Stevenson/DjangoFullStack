from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from topperApp.forms import UserForm, UserProfileForm, ReviewForm, AlbumForm, GenreForm
from topperApp.models import addAlbum, addReview, Genre, UserProfile, addAlbum
from django import forms
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
	return render(request, 'topper/index.html')

def about(request):
	context_dict = {'boldmessage': "About Page"}
	return render(request, 'topper/about.html', context = context_dict)
	
def contactUs(request):
	context_dict = {'boldmessage': "The Team"}
	return render(request, 'topper/contactus.html', context = context_dict)
	
def siteMap(request):
	context_dict = {'boldmessage': "Where do you want to go?"}
	return render(request, 'topper/sitemap.html', context = context_dict)
	
def topAlbums(request):
	context_dict = {'boldmessage': "Here you can find the top albums sorted by rating "}
	albums = addAlbum.objects.filter()
	sorted_albums = sorted(albums, key=lambda t: t.get_rating(), reverse=True)
	context_dict['topalbums'] = sorted_albums
	context_dict['AZalbums'] = addAlbum.objects.order_by('title')
	return render(request, 'topper/topalbums.html', context = context_dict)
	
def topReviewers(request):
	context_dict = {'boldmessage': "Here you can find the most active reviewers of each month"}
	return render(request, 'topper/topreviewers.html', context = context_dict)

def genre(request):
	topGenre_list = Genre.objects.order_by('-views')[:5]
	AZ_list = Genre.objects.order_by('genreName')
	context_dict = {'boldmessage': "Genres", 'genres': topGenre_list, 'AZgenres': AZ_list}
	response = render(request, 'topper/genre.html', context_dict)
	return response
	

@login_required	
def show_review(request, addReview_review_slug=None):
	context_dict = {}
	try:
		reviews = addReview.objects.get(slug=addReview_review_slug)
		albums = addAlbum.objects.filter(reviews=reviews)
		context_dict['albums'] = albums
		context_dict['add Review'] = reviews
	except addReview.DoesNotExist:
		context_dict['add Review'] = None
		context_dict['albums'] = None
	return render(request, 'topper/reviews.html', context_dict)

@login_required	
def add_Review(request, addAlbum_title_slug):
	try:
		albums = addAlbum.objects.get(slug=addAlbum_title_slug)
	except addAlbum.DoesNotExist:
		albums = None
	
		
		
	form = ReviewForm()
	if request.method == 'POST':
		form = ReviewForm(request.POST)
		if form.is_valid():
			if albums:
				try:
					reviews = form.save(commit=False)
					reviews.album = albums
					reviews.username = request.user
					reviews.save()
					return show_albums(request, addAlbum_title_slug)
				except:
					return HttpResponse("you already have a review on this album!")
		else:
			print(form.errors)
	context_dict = {'form': form,'albums': albums}
	return render(request, 'topper/add_review.html',  context_dict)

	
@login_required	
def add_Album(request):
	form = AlbumForm()
	if request.method == 'POST':
		form = AlbumForm(request.POST, request.FILES)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print(form.errors)
	return render(request, 'topper/add_album.html', {'form': form})


def show_albums(request, addAlbum_title_slug):
	context_dict = {}
	try:
		albums = addAlbum.objects.get(slug=addAlbum_title_slug)
		reviews = addReview.objects.filter(album=albums)
		context_dict['albums'] = albums
		context_dict['reviews'] = reviews
	except addAlbum.DoesNotExist:
		context_dict['albums'] = None
		context_dict['reviews'] = None
	return render(request, 'topper/album.html', context_dict)
	
#by Ruwaid, used for search album
def get_albums_list(max_results=0, starts_with=''):
	albums_list = []
	if starts_with:
		albums_list = addAlbum.objects.filter(name_istartswith=starts_with)
	
	if max_results > 0:
		if len(albums_list) > max_results:
			albums_list = album_list[:max_results]
	return albums_list
	
def show_genre(request, Genre_genreName_slug=None):
	context_dict = {}
	try:
		genre = Genre.objects.get(slug=Genre_genreName_slug)
		albums = addAlbum.objects.filter(genre=genre)
		albums = albums.order_by('title')
		context_dict['genre'] = genre
		context_dict['albums'] = albums
	except Genre.DoesNotExist:
		context_dict['genre'] = None
		context_dict['albums'] = None
	return render(request, 'topper/show_genre.html', context_dict)
	
#by Ruwaid, used for search album	
def suggest_albums(request):
	albums_list = []
	start_with = ""
	
	if request.method == 'GET':
		starts_with = request.GET['suggestion']
	albums_list = get_albums_list(8, starts_with)
	
	return render(request, 'topper/albums.html', {'albums': albums_list })
	
@login_required	
def account(request):
	context_dict = {'boldmessage': "Your Account"}
	return render(request, 'topper/account.html', context = context_dict)
	
def register(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data = request.POST)
		profile_form = UserProfileForm(data=request.POST)
		
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			#return redirect('index')
			profile = profile_form.save(commit = False)
			profile.user = user
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
				profile.save()
				registered = True
			else:
				print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render(request, 'topper/register.html',{ 'user_form':user_form, 'profile_form':profile_form,'registered':registered})
	
def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		
		if user:
			if user.is_active :
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Your Rango account is disabled.")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request, 'topper/login.html', {})

@login_required		
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))
	

