from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from categories.models import Category
from categories.api.serializer import  CategorySerializer
from categories.api.permisions import IsAdminOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response

class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    # queryset = Category.objects.all()
    # Vamos a hacer un filtro de las catergorias publicadas
    queryset = Category.objects.filter(published=True)
    
    # Estso cambia el id por slug
    lookup_field = 'slug'
    # Aca uso los filter de django_filter
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
    
    @action(methods=['patch'], detail=True)
    def toggle(self, request, slug):
        try:
            category =  self.get_object()
            print(category)
            category.published = not category.published
            category.save()
            return Response({"message": "Categoria actualizada"}, status=200)
        except Exception as e:
            raise e