Serializers
===========

.. module:: serializer
    :platform: Unix
    :synopsis: All serializer

All classes have a serializer.
Everyone has got the same structure:
For example we look at the **UserSerializer**

class UserSerializer(serializers.ModelSerializer):
--------------------------------------------------

They always have a inner class:
    **class Meta:**
with a Attribute *model = classname*
    **model = User**
and a Attribute *fields = ( attributes of the class )*
    **fields = ('username', 'password', 'email', 'age', 'gender')**

Serializers were used to put the data easier into the database.