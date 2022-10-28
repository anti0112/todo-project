from rest_framework import serializers
from goals.models import Goal
from core.serializers import UserSerializer

class GoalCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Goal
        fields = '__all__'
        read_only_fields = ('id', 'created', 'updated', 'user', 'description',)
        
    def validate_category(self, value):
        if value.is_deleted:
            raise serializers.ValidationError("not allowed in deleted category")
        
        if value.user != self.context['request'].user:
            raise serializers.ValidationError('not owner of category')
        
        return value
    

class GoalSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Goal
        fields = '__all__'
        read_only_fields = ('id', 'created', 'updated', 'user', 'description', 'category')
        
    