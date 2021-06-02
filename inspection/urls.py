from django.urls import path, include

from .views import (
                    homepage_view, 
                    ReportCreateView, 
                    ReportDetailView,
                    ReportListView,
                    ReportUpdateView,
                    )

urlpatterns = [
    path('', homepage_view, name='home'),
    path('report/add/', ReportCreateView.as_view(), name='create_report'),
    path('report/list/', ReportListView.as_view(), name='list_report'),
    path('report/update/<int:pk>', ReportUpdateView.as_view(), name='update_report'),
    path('report/<int:pk>/', ReportDetailView.as_view(), name='get_report'),
]