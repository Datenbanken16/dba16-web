Models
=======

**This are all classes and functions**

.. module:: models
    :platform: Unix
    :synopsis: All models


class User(models.Model):
-------------------------
    A Useraccount for access data to the homepage

    ==========  ===========
    Attributes  Description
    ==========  ===========
    username    The username the user choose
    password    The password the user choose
    email       The email of the user
    age         The age of the user
    gender      The gender of the user
    ==========  ===========

**Functions**

.. function:: __str__(self):

    Returns data of class User

    :return: username(string) - password(string) - email(string) - age(smallInt) - gender(string)


.. function:: save_forRegView(self, *args, **kwargs):

    Saves data from the registration view

    :param args: data of class User
    :param kwargs: keyword arguments
    :return: User -- Saves arguments


class Location(models.Model):
-----------------------------
    A Location for class Room(models.Model):the User

    =============       ===========
    Attributes          Description
    =============       ===========
    city                The city where the user is
    country_short       The abbreviation for the Country
    =============       ===========

class Room(models.ModelA Room the User is in):
----------------------------------------------
    A Room the User can be in

    =============       ===========
    Attributes          Description
    =============       ===========
    location            The location the user is at
    identifier          A identifier for the location
    =============       ===========

class Question(models.Model):
-----------------------------
    Questions for the User

    =============       ===========
    Attributes          Description
    =============       ===========
    question_text       The text for the question
    =============       ===========

class Choice(models.Model):
---------------------------
    The Choice the User can make for a Question

    ================        ===========
    Attributes              Description
    ================        ===========
    question                The question for the User
    choice_imagePath        The choice with maxlength 200
    ================        ===========

class UserAnswer(models.Model):
-------------------------------
    A Answer the User can give

    =============       ===========
    Attributes          Description
    =============       ===========
    user                The User who answers
    choice              The answer the user gives
    date                The date when the user make the answer
    =============       ===========

class Weather(models.Model):
----------------------------
    The Weather outside from a location

    =============       ===========
    Attributes          Description
    =============       ===========
    location            The location where the user is
    temperature         The temperature outside
    pressure            The pressure outsie
    humidity            The humidity outside
    windspeed           The windspeed at the moment
    winddegree          The winddegree at the moment
    date                The date for all datas
    =============       ===========

class SensorStepCount(models.Model):
------------------------------------
    The Steps the User made and Energie used

    ====================    ===========
    Attributes              Description
    ====================    ===========
    user                    The User we get data from
    start_time              The starttime we count from
    end_time                The endtime we count from
    time_offset             The time offset
    count                   The counted steps
    distance                The distance the user walked
    calorie                 The calories the user has burned
    speed                   The avarage speed he walked
    sample_position_type    The sample position type
    ====================    ===========

class SensorSleepStage(models.Model):
-------------------------------------
    The data of the sleep stages

    =============       ===========
    Attributes          Description
    =============       ===========
    user                The user we get the sleep data from
    start_time          The start time when the user enters a sleep stage
    end_time            The endtime of the sleepstage
    time_offset         The time offset
    sleep_id            A ID for the sleep stage
    stage               The stage the user was in while sleeping
    =============       ===========

class SensorSleep(models.Model):
--------------------------------
    The start and end time the user sleeps

    =============       ===========
    Attributes          Description
    =============       ===========
    user                The user we get the data from
    start_time          The time the user fall asleep
    end_time            The time when the user wakes up
    time_offset         The time offset
    =============       ===========

class SensorExercise(models.Model):
-----------------------------------
    The data from the user while doing sports

    ====================    ===========
    Attributes              Description
    ====================    ===========
    user                    The user we get the data from
    start_time              The time the user starts an exercise
    end_time                The time the user ends his exercise
    time_offset             The time offset
    calorie                 The calories burned
    duration                The duration from the exercise
    exercise_type           The type of exercise the user do
    exercise_custom_type    A custom exercise the user can do
    distance                The distance when the user walks or runs
    altitude_gain           The altitude he surmount
    altitude_loss           The height he gets down
    count                   The steps the user made
    count_type              The type how we count
    max_speed               The maximum speed the user
    mean_speed              The average speed of the User
    max_caloricburn_rate    The maximum rate of burned calories
    max_caloricburn_rate    The average rate of burned calories
    max_cadence             The maximum cadence while exercise
    mean_cadence            The average cadence while exercise
    max_heart_rate          The maximum heart rate of the User
    mean_heart_rate         The average heart rate of the User
    min_heart_rate          The minimum heart rate of the User
    max_altitude            The maximum altitude the user surmounted
    mean_altitude           The average altitude the user surmounted
    incline_distance        The distance of incline
    decline_distance        The distance of decline
    max_power               The maximum of power used
    mean_power              The average of power used
    mean_rpm                The average of rounds per minute
    location                The location where the data were send
    ====================    ===========

class SensorWaterIntake(models.Model):
--------------------------------------
    The Water the User drinks

    =============       ===========
    Attributes          Description
    =============       ===========
    user                The user we get the data from
    start_time          The start time when we count
    time_offset         The time offset
    amount              The amount the user drinks
    unit_amount         The unit we count the amount
    =============       ===========

class SensorFoodIntake(models.Model):
-------------------------------------
    The food the User eats

    =============       ===========
    Attributes          Description
    =============       ===========
    user                The user wer get the data from
    start_time          The start time when we count
    time_offset         The time offset
    calorie             The calories eaten
    food_info_id        The id of the food
    amount              The amount the user eats
    unit                The unit we count the amount
    name                The name of the meal
    meal_type           The type of the meal
    =============       ===========

class SensorCaffeineIntake(models.Model):
-----------------------------------------
    The value of caffeine the user takes

    =============       ===========
    Attributes          Description
    =============       ===========
    user                The user we get the data from
    start_time          The start time we count from
    time_offeset        The time offset
    amount              The amount the user takes
    unit_amount         The unit we count the amount
    =============       ===========

class SensorHeartRate(models.Model):
------------------------------------
    The data of the Heart Sensor

    ================    ===========
    Attributes          Description
    ================    ===========
    user                The user we get the data from
    start_time          The time we start to count
    end_time            The time we finish to count
    time_offset         The time offset
    heart_rate          The heart rate of the user
    heart_beat_count    The heart beat of the user
    ================    ===========

class SensorBodyTemperature(models.Model):
------------------------------------------
    The body temperature of the user

    =============       ===========
    Attributes          Description
    =============       ===========
    user                The user we get the data from
    start_time          The time we start to count
    time_offset         The time offset
    temperature         The body temperature of the user
    =============       ===========

class SensorBloodPressure(models.Model):
----------------------------------------
    Questions for the User

    =============       ===========
    Attributes          Description
    =============       ===========
    user                The user we get the data from
    start_time          The time we start to count
    time_offset         The time offset
    systolic            The systolic blood pressure
    diastolic           The diastolic blood pressure
    mean                The mean value
    pulse               The pulse of the user
    =============       ===========

class SensorHbA1c(models.Model):
--------------------------------
    The hbA1c value of the user

    =============       ===========
    Attributes          Description
    =============       ===========
    user                The user we get the data from
    start_time          The time we start to count
    time_offset         The time offset
    hba1c               The hba1c value of the user
    =============       ===========

class SensorBloodGlucose(models.Model):
---------------------------------------
    The glucose value of the user

    ==================  ===========
    Attributes          Description
    ==================  ===========
    user                The user we get the data from
    start_time          The time we start to count
    time_offset         The time offset
    glucose             The gluose value of the user
    meal_time           The time the user eats the meal
    meal_type           The type of the meal
    measurement_type    The type of measurement
    sample_source_type  The type of source
    ==================  ===========

class SensorOxygenSaturation(models.Model):
-------------------------------------------
    The Oxygen saturation the user has

    =============       ===========
    Attributes          Description
    =============       ===========
    user                The user we get the data from
    start_time          The time we start to count
    end_time            The time we finish to count
    time_offset         The time offset
    spo2                The spo2 value of the user
    heart_rate          The heart-rate of the user
    =============       ===========

class SensorAmbientTemperature(models.Model):
---------------------------------------------
    The data of a Room sensor

    =============       ===========
    Attributes          Description
    =============       ===========
    user                The user we get the data from
    start_time          The time we start to count
    time_offset         The time offset
    temperature         The temperature where the user is
    humidity            The humidity where the user is
    latitude            The latitude where the user is
    longtitude          The longtitude where the user is
    altitude            The altitude of the users position
    accuracy            The accuracy of the position
    =============       ===========

class SensorUvExposure(models.Model):
-------------------------------------
    UV Value for the user position

    =============       ===========
    Attributes          Description
    =============       ===========
    user                The user we get the data from
    start_time          The time we start to count
    time_offset         The time offset
    uv_index            The UV value
    latitude            The latitude where the user is
    longtitude          The longtitude where the user is
    altitude            The altitude of the users position
    accuracy            The accuracy of the position
    =============       ===========
