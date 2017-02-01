from rest_framework import serializers
from coreapp.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'age', 'gender')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('pk', 'question_text')


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('pk', 'choice_imagePath')


class QuestionChoiceSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ('pk', 'question_text', 'choices')


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ('user', 'choice', 'date')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('pk', 'city', 'country_short')


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('pk', 'identifier')


class LocationRoomSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True)

    class Meta:
        model = Location
        fields = ('pk', 'city', 'country_short', 'rooms')


class SensorStepCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorStepCount
        fields = ('calorie', 'count', 'distance', 'end_time', 'sample_position_type', 'speed', 'start_time', 'time_offset', 'user')


class SensorSleepStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorSleepStage
        fields = ('end_time', 'sleep_id', 'stage', 'start_time', 'time_offset', 'user')


class SensorSleepSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorSleep
        fields = ('end_time', 'start_time', 'time_offset', 'user')


class SensorExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorExercise
        fields = ('altitude_gain', 'altitude_loss', 'calorie', 'count', 'count_type', 'decline_distance', 'distance', 'duration', 'end_time', 'exercise_custom_type', 'exercise_type', 'incline_distance', 'location_data', 'max_altitude', 'max_cadence', 'max_caloricburn_rate', 'max_heart_rate', 'max_power', 'max_speed', 'mean_altitude', 'mean_cadence', 'mean_caloricburn_rate', 'mean_heart_rate', 'mean_power', 'mean_rpm', 'mean_speed', 'min_heart_rate', 'start_time', 'time_offset', 'user')


class SensorWaterIntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorWaterIntake
        fields = ('amount', 'start_time', 'time_offset', 'unit_amount', 'user')


class SensorFoodIntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorFoodIntake
        fields = ('amount', 'calorie', 'food_info_id', 'meal_type', 'name', 'start_time', 'time_offset', 'unit', 'user')


class SensorCaffeineIntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorCaffeineIntake
        fields = ('amount', 'start_time', 'time_offset', 'unit_amount', 'user')


class SensorHeartRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorHeartRate
        fields = ('end_time', 'heart_beat_count', 'heart_rate', 'start_time', 'time_offset', 'user')


class SensorBodyTemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorBodyTemperature
        fields = ('start_time', 'temperature', 'time_offset', 'user')


class SensorBloodPressureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorBloodPressure
        fields = ('diastolic', 'mean', 'pulse', 'start_time', 'systolic', 'time_offset', 'user')


class SensorHbA1cSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorHbA1c
        fields = ('hba1c', 'start_time', 'time_offset', 'user')


class SensorBloodGlucoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorBloodGlucose
        fields = ('glucose', 'meal_time', 'meal_type', 'measurement_type', 'sample_source_type', 'start_time', 'time_offset', 'user')


class SensorOxygenSaturationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorOxygenSaturation
        fields = ('end_time', 'heart_rate', 'spo2', 'start_time', 'time_offset', 'user')


class SensorAmbientTemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorAmbientTemperature
        fields = ('accuracy', 'altitude', 'humidity', 'latitude', 'longitude', 'start_time', 'temperature', 'time_offset', 'user')


class SensorUvExposureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorUvExposure
        fields = ('accuracy', 'altitude', 'latitude', 'longitude', 'start_time', 'time_offset', 'user', 'uv_index')