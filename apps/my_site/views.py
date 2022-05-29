from django.shortcuts import render
from apps.my_site.forms import UserCreateForm
from django.shortcuts import render

from apps.my_site.forms import UserCreateForm


def all_courses(request):
    return render(request, 'allCourses.html')


def authorization(request):
    return render(request, "authorization.html")


def contacts(request):
    return render(request, "contacts.html")


def dis_course(request):
    return render(request, "disCourse.html")


def dis_web(request):
    return render(request, "disWeb.html")


def index(request):
    return render(request, 'index.html')


def lin_course(request):
    return render(request, 'linCourse.html')


def lin_web(request):
    return render(request, "linWeb.html")


def prog_course(request):
    return render(request, 'progCourse.html')


def prog_web(request):
    return render(request, "progWeb.html")


def register(request):
    if request.method == 'GET':
        user_form = UserCreateForm(request.GET)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password1'])
            # Save the User object
            new_user.save()
            return render(request, 'index.html')
    else:
        user_form = UserCreateForm()
    return render(request, 'registration.html', {'user_form': user_form})


def send_form(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(request, 'sendForm.html', context={'num_visits': num_visits})


def webinar(request):
    return render(request, "webinar.html")
