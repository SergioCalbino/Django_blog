from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from posts.models import Post
from posts.api.serializer import PostSerializer
from posts.api.permisions import IsAdminOrReadOnly

class PostApiViewSet(ModelViewSet):
    permission_clases = [IsAdminOrReadOnly]
    serializer_class =  PostSerializer
    queryset = Post.objects.filter(published = True)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    # Ahora filtro por slug de categoria o por cagegoria en base al id
    filterset_fields = ['category','category__slug']
    # filterset_fields = ['category']
    