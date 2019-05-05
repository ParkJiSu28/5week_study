from rest_framework.viewsets import ReadOnlyModelViewSet,ModelViewSet
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import list_route,detail_route
from rest_framework.response import Response
# Create your views here.

class PostViewSet(ModelViewSet):
    queryset =Post.objects.all()
    serializer_class = PostSerializer

    @list_route()
    def public_list(self,request):
        qs =self.queryset.filter(is_public =True)
        serializers =self.get_serializer(qs,many=True)
        return Response(serializers.data)

    @list_route()
    def created_list(self,request):
        qs=self.queryset.filter()