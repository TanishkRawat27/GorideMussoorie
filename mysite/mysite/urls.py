from django.contrib import admin
from django.urls import path
from rent.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', site, name="site"),
    path('booking/', booking, name="booking"),
    path('pricing/', pricing, name="pricing"),
    path('bookcar/', bookcar, name="bookcar"),
    path('bookscooty/', bookscooty, name="bookscooty"),

    path('leanmore/', leanmore, name='leanmore'),

    path('learnmore/', learnmore, name='learnmore'),
]

# STATIC FILES (safe version)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)