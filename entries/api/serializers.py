import sre_compile
from rest_framework import serializers
from entries.models import EntryModel

class EntrySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    concept = serializers.CharField()
    amount = serializers.FloatField()
    datetime = serializers.DateTimeField()
    
    def create(self, validated_data):
        # Voy a salvar a validate dataclass
        instance = EntryModel(
            datetime = validated_data.get("datetime"),
            concept = validated_data.get("concept"),
            amount = validated_data.get("amount")
        )
        
        
        instance.save()
        return instance
        
    def update(self, instance, validated_data):
        # modifico instancia
        instance.datetime = validated_data.get("datetime")
        instance.concept = validated_data.get("concept")    
        instance.amount = validated_data.get("amount")
        
        instance.save()
        return instance
        
        
    