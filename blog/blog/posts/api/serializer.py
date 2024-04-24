from rest_framework import serializers
from posts.models import Post
from users.api.serializer import  UserSerializer
from categories.api.serializer import CategorySerializer

# Vamos a implementar que popule los datos del usuario del post
class  PostSerializer(serializers.ModelSerializer):
    # Con esta linea hago que popule
    user = UserSerializer()
    category = CategorySerializer()
    class Meta:
        model = Post
        fields = [ 'title', 'content', 'slug', 'miniature', 'created_at', 'published', 'user', 'category']
