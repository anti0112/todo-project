from rest_framework import serializers

from goals.models import Comment
from core.serializers import UserSerializer

class CommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Comment
        read_only_fields = ('id', 'user', 'created', 'updated')
        fields = '__all__'
        
    def validate_goal(self, value):
        if value.is_deleted:
            raise serializers.ValidationError("not allowed in deleted goal")

        if value.user != self.context["request"].user:
            raise serializers.ValidationError("not owner of the goal")

        return value
    
    
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fread_only_fields = ('id', 'user', 'created', 'updated')
        fields = '__all__'