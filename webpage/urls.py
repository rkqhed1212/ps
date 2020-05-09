from django.urls import path
from webpage import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('contact', views.Contact, name="contact"),
    path('service', views.service, name="service"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('pricing', views.pricing, name="pricing"),
    path('business', views.business, name="business"),
    path('personal', views.personal, name="personal"),
    # path('success', views.success, name ='success'),
]
