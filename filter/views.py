from rest_framework import generics
from .models import FilterPost
from .serializers import FilterPostSerializer
from rest_framework.filters import SearchFilter
    
# Create your views here.

class FilterPostAPIView(generics.ListCreateAPIView):
    queryset = FilterPost.objects.all()
    serializer_class =FilterPostSerializer
    filter_backends =[SearchFilter]
    search_fields = ['email']
    
class FilterPostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FilterPost.objects.all()
    serializer_class = FilterPostSerializer
    

    def get_queryset(self):
        qs =super().get_queryset()
        email =self.kwargs['email']
        qs = FilterPost.objects.filter(FilterPost__email=email)        
        return qs