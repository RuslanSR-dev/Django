from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from MainApp import views

urlpatterns = [
    path('', views.main),
    path('about/', views.about),
    path('item/<int:id>/', views.show_item, name="item-page"),
    path('items/', views.items_list),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
