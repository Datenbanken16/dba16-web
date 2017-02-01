from django.db import models



"""
.. module:: models
    :platform: Unix
    :synopsis: All models

"""
class User(models.Model):
    """A Useraccount for access data to the homepage

    Attributes:
        username            The username the user choose
        password            The password the user choose
        email               The email of the user
        age                 The age of the user
        gender              The gender of the user
    """
    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.SmallIntegerField()
    gender = models.CharField(max_length=1)

    def __str__(self):
        """Constructor for string operations

        :return: username(string) - password(string) - email(string) - age(smallInt) - gender(string)
        """
        return '%s %s %s %s %s' % (self.username, self.password, self.email, self.age, self.gender)

    def save_forRegView(self, *args, **kwargs):
        """ Saves data from the registration view

        :param args: data of class User
        :param kwargs: keyword arguments
        :return: User -- Saves arguments
        """
        self.username = self.username.strip()
        self.password = self.password.strip()
        self.email = self.email.strip()
        try:
            self.age = self.age.strip()
        except:
            pass
        

        if self.username == '':
            raise ValueError("username must not be blank!")
        elif self.password == '':
            raise ValueError("password must not be blank!")
        elif self.email == '':
            raise ValueError("email must not be blank!")

        ageAsInt = 0
        try:
            ageAsInt = int(self.age)
        except:
            raise ValueError("age must be an integer value")

        if ageAsInt < 1 or ageAsInt > 110:
            raise ValueError("age has an unrealistic value!")
        elif self.gender != 'm' and self.gender != 'f':
            raise ValueError("field 'gender' has to be 'm' or 'f'")
        else:
            super(User, self).save(*args, **kwargs)


class Location(models.Model):
    """A Location for the User

        Attributes:
            city                The city where the user is
            country_short       The abbreviation for the Country
    """
    city = models.CharField(max_length=20)
    country_short = models.CharField(max_length=2)


class Room(models.Model):
    """A Room the User can be in

        Attributes:
            location            The location the user is at
            identifier          A identifier for the location
    """
    location = models.ForeignKey(Location, related_name='rooms', on_delete=models.CASCADE)
    identifier = models.CharField(max_length=200)


class Question(models.Model):
    """Questions for the User

        Attributes:
            question_text       The text for the question
    """
    question_text = models.CharField(max_length=200)

class Choice(models.Model):
    """The Choice the User can make for a Question

        Attributes:
            question            The question for the User
            choice_imagePath    The choice with maxlength 200
    """
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_imagePath = models.CharField(max_length=200)


class UserAnswer(models.Model):
    """A Answer the User can give

        Attributes:
            user                The User who answers
            choice              The answer the user gives
            date                The date when the user make the answer
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, blank=True)


class Weather(models.Model):
    """The Weather outside from a location

        Attributes:
            location            The location where the user is
            temperature         The temperature outside
            pressure            The pressure outside
            humidity            The humidity outside
            windspeed           The windspeed at the moment
            winddegree          The winddegree at the moment
            date                The date for all datas
    """
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    pressure = models.SmallIntegerField()
    humidity = models.SmallIntegerField()
    windspeed = models.DecimalField(max_digits=5, decimal_places=2)
    winddegree = models.SmallIntegerField()
    date = models.DateTimeField(auto_now=True, blank=True)


class SensorStepCount(models.Model):
    """The Steps the User made and Energie used

        Attributes:
            user                The User we get data from
            start_time          The starttime we count from
            end_time            The endtime we count from
            time_offset         The time offset
            count               The counted steps
            distance            The distance the user walked
            calorie             The calories the user has burned
            speed               The avarage speed he walked
            sample_position_type    The sample position type
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    time_offset = models.IntegerField()
    count = models.SmallIntegerField()
    distance = models.FloatField()
    calorie = models.FloatField()
    speed = models.FloatField()
    sample_position_type = models.SmallIntegerField()


class SensorSleepStage(models.Model):
    """The data of the sleep stages

        Attributes:
            user                The user we get the sleep data from
            start_time          The start time when the user enters a sleep stage
            end_time            The endtime of the sleepstage
            time_offset         The time offset
            sleep_id            A ID for the sleep stage
            stage               The stage the user was in while sleeping
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    time_offset = models.IntegerField()
    sleep_id = models.CharField(max_length=36)
    stage = models.SmallIntegerField()


class SensorSleep(models.Model):
    """The start and end time the user sleeps

        Attributes:
            user                The user we get the data from
            start_time          The time the user fall asleep
            end_time            The time when the user wakes up
            time_offset         The time offset
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    time_offset = models.IntegerField()


class SensorExercise(models.Model):
    """The data from the user while doing sports

        Attributes:
            user                The user we get the data from
            start_time          The time the user starts an exercise
            end_time            The time the user ends his exercise
            time_offset         The time offset
            calorie             The calories burned
            duration            The duration from the exercise
            exercise_type       The type of exercise the user do
            exercise_custom_type    A custom exercise the user can do
            distance            The distance when the user walks or runs
            altitude_gain       The altitude he surmount
            altitude_loss       The height he gets down
            count               The steps the user made
            count_type          The type how we count
            max_speed           The maximum speed the user
            mean_speed          The average speed of the User
            max_caloricburn_rate    The maximum rate of burned calories
            max_caloricburn_rate    The average rate of burned calories
            max_cadence         The maximum cadence while exercise
            mean_cadence        The average cadence while exercise
            max_heart_rate      The maximum heart rate of the User
            mean_heart_rate     The average heart rate of the User
            min_heart_rate      The minimum heart rate of the User
            max_altitude        The maximum altitude the user surmounted
            mean_altitude       The average altitude the user surmounted
            incline_distance    The distance of incline
            decline_distance    The distance of decline
            max_power           The maximum of power used
            mean_power          The average of power used
            mean_rpm            The average of rounds per minute
            location            The location where the data were send
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    time_offset = models.IntegerField()
    calorie = models.FloatField()
    duration = models.SmallIntegerField()
    exercise_type = models.SmallIntegerField()
    exercise_custom_type = models.CharField(max_length=255, null=True, blank=True)
    distance = models.FloatField()
    altitude_gain = models.FloatField()
    altitude_loss = models.FloatField()
    count = models.SmallIntegerField()
    count_type = models.SmallIntegerField()
    max_speed = models.FloatField()
    mean_speed = models.FloatField()
    max_caloricburn_rate = models.FloatField(null=True, blank=True)
    mean_caloricburn_rate = models.FloatField(null=True, blank=True)
    max_cadence = models.FloatField()
    mean_cadence = models.FloatField()
    max_heart_rate = models.FloatField(null=True, blank=True)
    mean_heart_rate = models.FloatField(null=True, blank=True)
    min_heart_rate = models.FloatField(null=True, blank=True)
    max_altitude = models.FloatField()
    mean_altitude = models.FloatField()
    incline_distance = models.FloatField()
    decline_distance = models.FloatField()
    max_power = models.FloatField(null=True, blank=True)
    mean_power = models.FloatField(null=True, blank=True)
    mean_rpm = models.FloatField(null=True, blank=True)
    location_data = models.CharField(max_length=255)


class SensorWaterIntake(models.Model):
    """The Water the User drinks

        Attributes:
            user                The user we get the data from
            start_time          The start time when we count
            time_offset         The time offset
            amount              The amount the user drinks
            unit_amount         The unit we count the amount
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    time_offset = models.IntegerField()
    amount = models.FloatField()
    unit_amount = models.FloatField()


class SensorFoodIntake(models.Model):
    """The food the User eats

        Attributes:
            user                The user wer get the data from
            start_time          The start time when we count
            time_offset         The time offset
            calorie             The calories eaten
            food_info_id        The id of the food
            amount              The amount the user eats
            unit                The unit we count the amount
            name                The name of the meal
            meal_type           The type of the meal
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    time_offset = models.IntegerField()
    calorie = models.FloatField()
    food_info_id = models.CharField(max_length=48)
    amount = models.FloatField()
    unit = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    meal_type = models.IntegerField()


class SensorCaffeineIntake(models.Model):
    """The value of caffeine the user takes

        Attributes:
            user                The user we get the data from
            start_time          The start time we count from
            time_offeset        The time offset
            amount              The amount the user takes
            unit_amount         The unit we count the amount
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    time_offset = models.IntegerField()
    amount = models.FloatField()
    unit_amount = models.FloatField()


class SensorHeartRate(models.Model):
    """The data of the Heart Sensor

        Attributes:
            user                The user we get the data from
            start_time          The time we start to count
            end_time            The time we finish to count
            time_offset         The time offset
            heart_rate          The heart rate of the user
            heart_beat_count    The heart beat of the user
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    time_offset = models.IntegerField()
    heart_rate = models.FloatField()
    heart_beat_count = models.SmallIntegerField()


class SensorBodyTemperature(models.Model):
    """The body temperature of the user

        Attributes:
            user                The user we get the data from
            start_time          The time we start to count
            time_offset         The time offset
            temperature         The body temperature of the user
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    time_offset = models.IntegerField()
    temperature = models.FloatField()


class SensorBloodPressure(models.Model):
    """Questions for the User

        Attributes:
            user                The user we get the data from
            start_time          The time we start to count
            time_offset         The time offset
            systolic            The systolic blood pressure
            diastolic           The diastolic blood pressure
            mean                The mean value
            pulse               The pulse of the user
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    time_offset = models.IntegerField()
    systolic = models.FloatField()
    diastolic = models.FloatField()
    mean = models.FloatField()
    pulse = models.SmallIntegerField()


class SensorHbA1c(models.Model):
    """The hbA1c value of the user

        Attributes:
            user                The user we get the data from
            start_time          The time we start to count
            time_offset         The time offset
            hba1c               The hba1c value of the user
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    time_offset = models.IntegerField()
    hba1c = models.FloatField()


class SensorBloodGlucose(models.Model):
    """The glucose value of the user

        Attributes:
            user                The user we get the data from
            start_time          The time we start to count
            time_offset         The time offset
            glucose             The gluose value of the user
            meal_time           The time the user eats the meal
            meal_type           The type of the meal
            measurement_type    The type of measurement
            sample_source_type  The type of source
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    time_offset = models.IntegerField()
    glucose = models.FloatField()
    meal_time = models.DateTimeField()
    meal_type = models.SmallIntegerField()
    measurement_type = models.SmallIntegerField()
    sample_source_type = models.SmallIntegerField()


class SensorOxygenSaturation(models.Model):
    """The Oxygen saturation the user has

        Attributes:
            user                The user we get the data from
            start_time          The time we start to count
            end_time            The time we finish to count
            time_offset         The time offset
            spo2                The spo2 value of the user
            heart_rate          The heart-rate of the user
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    time_offset = models.IntegerField()
    spo2 = models.FloatField()
    heart_rate = models.FloatField()


class SensorAmbientTemperature(models.Model):
    """The data of a Room sensor

        Attributes:
            user                The user we get the data from
            start_time          The time we start to count
            time_offset         The time offset
            temperature         The temperature where the user is
            humidity            The humidity where the user is
            latitude            The latitude where the user is
            longtitude          The longtitude where the user is
            altitude            The altitude of the users position
            accuracy            The accuracy of the position

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    time_offset = models.IntegerField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    altitude = models.FloatField(null=True, blank=True)
    accuracy = models.FloatField(null=True, blank=True)


class SensorUvExposure(models.Model):
    """UV Value for the users position

        Attributes:
            user                The user we get the data from
            start_time          The time we start to count
            time_offset         The time offset
            uv_index            The UV value
            latitude            The latitude where the user is
            longtitude          The longtitude where the user is
            altitude            The altitude of the users position
            accuracy            The accuracy of the position
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    time_offset = models.IntegerField()
    uv_index = models.FloatField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    altitude = models.FloatField(null=True, blank=True)
    accuracy = models.FloatField(null=True, blank=True)
