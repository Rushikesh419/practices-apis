# generic api view model mixin
from .models import Movie
from .serializer import Movieserializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin


# list and create - PK Not required
class LCMovieAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Movie.objects.all()
    serializer_class=Movieserializer
    
    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)

    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

# retrive update and common
class RUDSovieAPI(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Movie.objects.all()
    serializer_class=Movieserializer
    
    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)

    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)
    

# this is for seprate classes
# class MovieList(GenericAPIView,ListModelMixin):
#     queryset=Movie.objects.all()
#     serializer_class=Movieserializer
    
#     def get(self,request,*args, **kwargs):
#         return self.list(request,*args, **kwargs)
    
# class MovieCreate(GenericAPIView,CreateModelMixin):
#     queryset=Movie.objects.all()
#     serializer_class=Movieserializer
    
#     def post(self,request,*args, **kwargs):
#         return self.create(request,*args, **kwargs)
    
# class MovieRetrive(GenericAPIView,RetrieveModelMixin):
#     queryset=Movie.objects.all()
#     serializer_class=Movieserializer
    
#     def get(self,request,*args, **kwargs):
#         return self.retrieve(request,*args, **kwargs)
    
    
# class MovieUpdate(GenericAPIView,UpdateModelMixin):
#     queryset=Movie.objects.all()
#     serializer_class=Movieserializer
    
#     def put(self,request,*args, **kwargs):
#         return self.update(request,*args, **kwargs)
    
# class MovieDestroy(GenericAPIView,DestroyModelMixin):
#     queryset=Movie.objects.all()
#     serializer_class=Movieserializer
    
#     def delete(self,request,*args, **kwargs):
#         return self.destroy(request,*args, **kwargs)