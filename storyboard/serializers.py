from rest_framework import serializers
from storyboard.models import Plot, Character, Submission


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['name', 'bio']
        
class PlotSerializer(serializers.ModelSerializer):
    characters = CharacterSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = Plot
        fields = '__all__'

    def create(self, validated_data):
        characters = validated_data.pop('characters')
        plot = Plot.objects.create(**validated_data)
        for character in characters:
            Character.objects.create(plot=plot, **character)
        return plot

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'
