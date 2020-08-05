from django.conf.urls import url
from topperApp import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/', views.about, name='about'),
	url(r'^contactus/', views.contactUs, name='contactus'),
	url(r'^sitemap/', views.siteMap, name='sitemap'),
	url(r'^topalbums/', views.topAlbums, name='topalbums'),#i have made a show_album view so could link this url to that -ben
	url(r'^topreviewers/', views.topReviewers, name='topreviewers'),
	url(r'^genre/(?P<Genre_genreName_slug>[\w\-]+)/$', views.show_genre, name='show_genre'),
	url(r'^genre/', views.genre, name='genre'),
	url(r'^account/', views.account, name='account'),
	url(r'^register/', views.register, name='register'),
	url(r'^login/', views.user_login, name='login'),
	url(r'^add_album/', views.add_Album, name='add_album'),
	url(r'^review_album/', views.add_Review, name='review_album'),
	url(r'^reviews/', views.show_review, name='reviews'),
	url(r'^reviews/(?P<addReview_review_slug>[\w\-]+)/$', views.show_review, name='reviews'),
	url(r'^reviews/(?P<addReview_review_slug>[\w\-]+)/add_album/$',views.add_Album,name='add_album'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^suggest/$', views.suggest_albums, name='suggest_albums'),
	url(r'^album/(?P<addAlbum_title_slug>[\w\-]+)/$', views.show_albums, name='show_albums'),
	url(r'^album/(?P<addAlbum_title_slug>[\w\-]+)/add_review/$', views.add_Review, name='add_review'),
]
