
from rest_framework import serializers
from form.models import FormPage


class homeSerializer(serializers.ModelSerializer):

    class Meta:
        model = FormPage
        fields = ('firstname','lastname')
        # fields = '__all__'
