from django.urls import path
from .views import *

app_name = 'apps.my_site'

urlpatterns = [
    path('', index, name="index"),
    path('allCourses/', all_courses, name="allCourses"),
    path('authorization/', authorization, name="authorization"),
    path('contacts/', contacts, name="contacts"),
    path('disCourse/', dis_course, name="disCourse"),
    path('disWeb/', dis_web, name="disWeb"),
    path('linCourse/', lin_course, name="linCourse"),
    path('linWeb/', lin_web, name="linWeb"),
    path('progCourse/', prog_course, name="progCourse"),
    path('progWeb/', prog_web, name="progWeb"),
    path('registration/', register, name="registration"),
    path('sendForm/', send_form, name="sendForm"),
    path('webinar/', webinar, name="webinar"),

    # path('', MovieList.as_view(), name='movie_list'),
    # path(r'<int:pk>/', MovieDetailView.as_view(), name='movie_details'),
    # path(r'add/movies', MovieAddView.as_view(), name='movie_add'),
    # path(r'add/person', PersonAddView.as_view(), name='person_add'),
    # path('long_running/', LongRunning.as_view(), name='long_running'),
    # path('rank/', movie_and_person_rank, name='movie_and_person_rank')
]
