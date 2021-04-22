from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="shophome"),
    path("about/",views.about,name="Aboutus"),
    path("contact/",views.contact,name="Contactus"),
    path("tracker/",views.tracker,name="Trackestatus"),
    path("search/",views.search,name="Search"),
    path("productview/",views.productview,name="Productview"),
    path("checkout/",views.checkout,name="Checkout")
]