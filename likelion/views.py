from rest_framework.viewsets import ReadOnlyModelViewSet,ModelViewSet
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import list_route,detail_route
from rest_framework.response import Response
# Create your views here.
from rest_framework.filters import SearchFilter
class PostViewSet(ModelViewSet):
    queryset =Post.objects.all()
    serializer_class = PostSerializer
    filter_backends =[SearchFilter]
    search_fields = ['title']

    @list_route()
    def public_list(self,request):
        qs =self.queryset.filter(is_public =True)
        serializers =self.get_serializer(qs,many=True)
        return Response(serializers.data)

   # def get_queryset(self):
        qs=super().get_queryset()
        if self.request.user.is_authenticated:
            qs = qs.filter(author =self.request.user)
        else:
            qs=qs.none() #empty result
        return qs
    