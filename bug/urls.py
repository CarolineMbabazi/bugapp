from django.urls import path
from .views import bug_submission, bug_list, bug_details

urlpatterns = [
    path('', bug_list, name='list_bugs'),
    path('add/', bug_submission, name = 'add_bug'),
    path('bug/<int:pk>/', bug_details, name = 'detail_view'),
]
