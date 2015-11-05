from django.conf.urls import url

from . import views
urlpatterns = [
	url(r'^masterdata_carwale/', views.masterdata_carwale, name='masterdata_carwale'),
	url(r'^carwale_scrap/', views.carwale_scrap, name='carwale_scrap'),
	url(r'^carwale_update/', views.carwale_update, name='carwale_update'),
	url(r'^carwale_delete/', views.carwale_delete, name='carwale_delete'),
	url(r'^carwale_active/', views.carwale_active, name='carwale_active'),
	url(r'^master_cartrade/', views.masterdata_cartrade, name='masterdata_cartrade'),
	url(r'^cartrade/', views.cartrade_scrap, name='cartrade_scrap'),
	url(r'^cartrade_update/', views.cartrade_update, name='cartrade_update'),
	url(r'^cartrade_delete/', views.cartrade_delete, name='cartrade_delete'),
	url(r'^cartrade_active/', views.cartrade_active, name='cartrade_active'),

	]