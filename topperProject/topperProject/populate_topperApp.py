import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','Topper.settings')
import django
django.setup()


from topperApp.models import addAlbum, addReview, UserProfile, Genre


def populate():
	#userprofiles = [ 
	#{"user": "Stacy",
	#"picture": settings.MEDIA_ROOT/profile_images/filename.jpeg},
	#{"user": "Marshall",
	#"picture": settings.MEDIA_ROOT/profile_images/filename.jpeg} ]
	
	blues_albums = [
		{"title": "Human",
		"artist": "Rag'n'Bone Man",
		"ratings":0}]
	pop_albums = [
		{"title": "25",
		"artist": "Adele",
		"ratings":0},
		{"title": "I Like It When You Sleep, for You Are So Beautiful yet So Unaware of It",
		"artist": "The 1975",
		"ratings": 0},
		{"title": "Lemonade",
		"artist": "Beyonce",
		"ratings": 0},
		{"title": "Divide",
		"artist": "Ed Sheeran",
		"ratings":0},
		{"title": "Glory Days",
		"artist": "Little Mix",
		"ratings":0}]
	rock_albums = [
		{"title": "Nightmare",
		"artist": "Avenged Sevenfold",
		"ratings":0},
		{"title": "Nevermind",
		"artist": "Nirvana",
		"ratings":0},
		{"title": "Pink Floyd",
		"artist": "The Dark Side of the Moon",
		"ratings":0},
		{"title": "Immortalized",
		"artist": "Disturbed",
		"ratings":0},
		{"title": "American Idiot",
		"artist": "Green Day",
		"ratings":0}]
	hiphop_albums = [
		{"title": "Views",
		"artist": "Drake",
		"ratings":0},
		{"title": "Gang Signs & Prayer",
		"artist": "Stormzy",
		"ratings":0}]
	edm_albums = [
		{"title": "Stuff I Used to Do",
		"artist": "Deadmau5",
		"ratings":0},
		{"title": "Collage (EP)",
		"artist": "The Chainsmokers",
		"ratings":0},
		{"title": "Encore",
		"artist": "DJ Snake",
		"ratings":0}]
	poppunk_albums = [
		{"title": "Enema of the State",
		"artist": "Blink 182",
		"ratings":0},
		{"title": "The Young and The Hopeless",
		"artist": "Good Charlotte",
		"ratings":0},
		{"title": "American Psycho",
		"artist": "Fall Out Boy",
		"ratings":0}]
	indie_albums = [
		{"title": "(What's The Story) Morning Glory",
		"artist": "Oasis",
		"ratings":0},
		{"title": "Different Creatures",
		"artist": "Circa Waves",
		"ratings":0},
		{"title": "Kasabian",
		"artist": "Kasabian",
		"ratings":0}]

	genres = {
		"Blues": {"albums": blues_albums,
					   "views":3,},
		"Pop": {"albums": pop_albums,
					   "views":11,},
		"Rock": {"albums": rock_albums,
					   "views":4,},
		"Hip-Hop": {"albums": hiphop_albums,
					   "views":6,},
		"EDM": {"albums": edm_albums,
					   "views":3,},
		"Pop Punk": {"albums": poppunk_albums,
					   "views":2,},
		"Indie": {"albums": indie_albums,
					   "views":4,} }
					  

	

	
	#for user_data in user:
	#	c = adduser(user_data["user"], user_data["picture"])
		
	for genre, genre_data in genres.items():
		g = addgenre(genre, genre_data["albums"], genre_data["views"])
		for p in genre_data["albums"]:
			addalbum(g, p["title"], p["artist"], p["ratings"])
	
	for g in Genre.objects.all():
		for p in addAlbum.objects.filter(title=genres):
			print("- {0} - {1}".format(str(g), str(p)))
	
	
def adduser(user, path_to_picture):
	c = UserProfile.objects.get_or_create(user=user)[0]
	image = open(path_to_picture, "rb")
	dimage = File(image)
	c.picture = dimage
	c.save()
	return c
	
def addalbum(g, title, artist, ratings=0):
	a = addAlbum.objects.get_or_create(title=title, artist=artist, genre=g)[0]
	a.save()
	return a
	
def addgenre(genreName, albums, views=0):
	g = Genre.objects.get_or_create(genreName=genreName, views=views)[0]
	g.save()
	return g
	
if __name__ == '__main__':
	print("Starting population script for topper, this may take a while.")
	populate()
	
