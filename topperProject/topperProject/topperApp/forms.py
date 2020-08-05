from django.contrib.auth.models import User
from topperApp.models import  UserProfile, addAlbum, addReview, Genre
from django import forms


class ReviewForm(forms.ModelForm):
	review = forms.CharField(max_length=128,help_text="Please enter your review.")
	rating = forms.IntegerField(required=True)
	
	
	
	class Meta:
		model = addReview
		fields = ('review','rating',)

class AlbumForm(forms.ModelForm):
	title = forms.CharField(max_length=128, help_text="Please enter the title of the Album.")
	artist = forms.CharField(max_length=128, help_text="Please enter the artist of the Album.")
	Genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all())
	slug =forms.CharField(widget=forms.HiddenInput(), required=False)
	
	class Meta:
		model = addAlbum
		fields = ('title','artist','genre','image',)

class GenreForm(forms.ModelForm):
    genres = forms.CharField(max_length=128 , help_text = "Add new genre.")

    class Meta:
        model = Genre
        fields = ("genres",)

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = User
		fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('picture',)
