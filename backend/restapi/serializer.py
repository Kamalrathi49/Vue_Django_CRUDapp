from restapi.models import *
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    # def to_representation(self, instance):
    #     representation = super(ClientSerializer, self).to_representation(instance)
    #     representation['created_on'], representation['created_by']  = instance.created_on.strftime("%d %B, %Y"), instance.created_by.username
    #     return representation

