from rest_framework import serializers

from myapp.models import User


class UserSerializer(serializers.ModelSerializer):

    old_password = serializers.CharField(write_only=True, required=False)
    date_joined = serializers.CharField(read_only=True)

    def validate(self, data):
        request_method = self.context['request'].method
        password = data.get('password', None)
        if request_method == 'POST':
            if password == None:
                raise serializers.ValidationError(
                    {"info": "Please provide a password."})
        elif (request_method == 'PUT' or request_method == 'PATCH'):
            old_password = data.get('old_password', None)
            if password != None and old_password == None:
                raise serializers.ValidationError(
                    {"info": "Please provide the old password."})
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user

    def update(self, instance, validated_data):
        try:
            user = instance
            if 'password' in validated_data:
                password = validated_data.pop('password')
                old_password = validated_data.pop('old_password')
                if user.check_password(old_password):
                    user.set_password(password)
                else:
                    raise Exception("Old password is incorrect.")
                user.save()
        except Exception as err:
            raise serializers.ValidationError({"info": err})
        return super(UserSerializer, self).update(instance, validated_data)

    class Meta:
        model = User
        fields = ['id', 'is_superuser', 'username',
                  'email', 'password', 'old_password', 'date_joined']
        extra_kwargs = {
            'password': {'write_only': 'true'}
        }
