Views
=====

**Here are the functions for the views**

.. module:: views
    :platform: Unix
    :synopsis: All views

class JSONResponse(HttpResponse):
_________________________________
    An HttpResponse that renders its content into JSON.

**Functions**

.. function:: __init__(self, data, **kwargs):

    Constructor for string operations

    :param data: data to render for JSON
    :param kwargs: keyword arguments

.. function:: user_list(request):

    List all users, or create a new user.

    :param request: HttpRequest , Get or Post
    :return: JSONResponse(serializer,data)
    :return: JSONResponse(serializer.data, status=201)
    :return: JSONResponse(serializer.errors, status=400)

.. function:: user_detail(request, pk):

    Retrieve, update or delete userdata.

    :param request: User data
    :param pk: Primary Key of the User
    :return: HttpResponse(status=404) = error
    :return: JSONResponse(serializer.data) = accept
    :return: JSONResponse(serializer.errors, status=400) = error
    :return: return HttpResponse(status=204) = accept

.. function:: auth_check(request):

    Checks the authentication.

    :param request: Userdata for authentification
    :return: JSONResponse(content) = auth. failt or passed
    :return: HttpResponse(status=404) = Error

.. function:: user_login(request):

    Checks datas from login page and gives ja session-id

    :param request: Userdata from login
    :return: session-id

.. function:: user_logout(request):

    Logs the user out and deletes the session

    :param request: Logout action
    :return: reload with passed message

.. function:: show_home(request):

    Show the home screen.

    :param request: Request for entering homescreen
    :return: render homescreen

.. function:: show_profile(request):

    Show the Profile page of the user

    :param request: Request for entering Profile
    :return: render Profilescreen - if accept
    :return: render Login - if no session-id

.. function:: show_user_registration_form(request):

    Show the user Registration page.

    :param request: Request for the Registration-view
    :return: render Registration - if accept
    :return: render Login - if registratet

.. function:: question_add(request):

    Add a new question to the app.

    :param request: the new question
    :return: true or false

.. function:: question_answer(request):

    Add question Answers to the app.

    :param request: the new answer
    :return: true or false

.. function:: room_add(request, pk):

    Add a new Room.

    :param request: Room data
    :param pk: Primary Key for the new Room
    :return: true or false

.. function:: weather_add(request, pk):

    Saves the weather data from the moment.

    :param request: weatherdata
    :param pk: Primary Key for the data
    :return: true or false

.. function:: TablesPageView(request):

    Renders the view for the Table-Page.

    :param request: Request for Table-Page
    :return: TablePage
