from django.conf.urls import url

from . import views
urlpatterns = [
	url(r'^master_data/', views.master_data, name='master_data'),
	url(r'^carwale/', views.carwale, name='carwale')
	]