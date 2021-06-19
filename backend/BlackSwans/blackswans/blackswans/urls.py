from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pagerank', views.top10_papers_by_pagerank_by_cites),
    path('pr-journal', views.top10_papers_by_pagerank_by_journal),
    path('anomalies', views.anomalies),
]
