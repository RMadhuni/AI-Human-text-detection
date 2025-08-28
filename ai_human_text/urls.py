from django.contrib import admin
from django.urls import path
from text_detection import views  # ✅ correct import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('review/', views.review, name='review'),
    path('contact/', views.contact, name='contact'),
    path('generate_report/', views.generate_report, name='generate_report'),  # ← NEW

]
