from django import template
from topperApp.models import addAlbum

register = template.Library()

@register.inclusion_tag('topper/albums.html')
def get_albums_list(Albums=None):
	return {'Albums': addAlbum.objects.all(),
			'act_Albums': Albums}