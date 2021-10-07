from rest_framework.serializers import ModelSerializer
from .models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note # import the model you want to serialize
        fields = '__all__' # specify fields you want to serialize. ['body', 'updated', 'created'] if you'd like to serialize only some of fields, but not all.
