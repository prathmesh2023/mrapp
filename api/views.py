from unicodedata import name
from urllib import response
from urllib.request import Request
from django.shortcuts import render
from app1.models import mr_user, visit,dr_user
from app1.models import testing,slide,ppt

from api.serializers import testingSerializer
from api.serializers import mr_userSerializer
from api.serializers import dr_userSerializer
from api.serializers import visitSerializer
from api.serializers import slideSerializer
from api.serializers import mrloginSerializer,pptSerializer,visit_mrSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import json

from rest_framework import viewsets

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


# class TestingViewSet(viewsets.ModelViewSet):

#     queryset = testing.objects.all()
#     serializer_class = testingSerializer

#     # authentication_class = [TokenAuthentication]
#     # permission_class = [IsAuthenticated]




class mr_userClassBassedView(APIView):

    def get(self, request, id=None ,format=None):
        if id is not None:
            
            try:
                tt = mr_user.objects.get(id=id)
            except:
                return Response('no data found', status=status.HTTP_404_NOT_FOUND)

            s = mr_userSerializer(tt,many=False)

            return Response(s.data, status=status.HTTP_200_OK)
        tt= mr_user.objects.all()
        s = mr_userSerializer(tt, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request, id=None ,format=None):
        s = mr_userSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)

        return Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    
    def put(self, request, id=None ,format=None):
        try:
            tt=mr_user.objects.get(id=id)
        except:
            return Response("no data found ", status=status.HTTP_404_NOT_FOUND)
        s = mr_userSerializer(instance=tt, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    
    def delete(self, request, id=None ,format=None):
        try:
            tt= mr_user.objects.get(id=id)
        except:
            return Response("no data found ", status=status.HTTP_404_NOT_FOUND)
        tt.delete()
        return Response("deleted", status=status.HTTP_201_CREATED)


class dr_userClassBassedView(APIView):

    def get(self, request, id=None ,format=None):
        if id is not None:
            
            try:
                tt = dr_user.objects.get(id=id)
            except:
                return Response('no data found', status=status.HTTP_404_NOT_FOUND)

            s = dr_userSerializer(tt,many=False)

            return Response(s.data, status=status.HTTP_200_OK)
        tt= dr_user.objects.all()
        s = dr_userSerializer(tt, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request, id=None ,format=None):
        s = dr_userSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)

        return Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    
    def put(self, request, id=None ,format=None):
        try:
            tt=dr_user.objects.get(id=id)
        except:
            return Response("no data found ", status=status.HTTP_404_NOT_FOUND)
        s = dr_userSerializer(instance=tt, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    
    def delete(self, request, id=None ,format=None):
        try:
            tt= dr_user.objects.get(id=id)
        except:
            return Response("no data found ", status=status.HTTP_404_NOT_FOUND)
        tt.delete()
        return Response("deleted", status=status.HTTP_201_CREATED)


class visitClassBassedView(APIView):

    def get(self, request, id=None ,format=None):
        if id is not None:
            
            try:
                tt = visit.objects.get(id=id)
            except:
                return Response('no data found', status=status.HTTP_404_NOT_FOUND)

            s = visitSerializer(tt,many=False)

            return Response(s.data, status=status.HTTP_200_OK)
        tt= visit.objects.all()
        s = visitSerializer(tt, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request, id=None ,format=None):
        s = visitSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)

        return Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    
    def put(self, request, id=None ,format=None):
        try:
            tt=visit.objects.get(id=id)
        except:
            return Response("no data found ", status=status.HTTP_404_NOT_FOUND)
        s = visitSerializer(instance=tt, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    
    def delete(self, request, id=None ,format=None):
        try:
            tt= visit.objects.get(id=id)
        except:
            return Response("no data found ", status=status.HTTP_404_NOT_FOUND)
        tt.delete()
        return Response("deleted", status=status.HTTP_201_CREATED)





class mrloginClassBassedView(APIView):

    def get(self, request, user_name=None ,password=None, format=None):
        if user_name and password is not None:
            
            try:
                tt = mr_user.objects.get(user_name=user_name, password=password)
            except:
                response_data = {}
                response_data['message'] = "user not found" 
                return HttpResponse(json.dumps(response_data), content_type="application/json")
                # return Response('no data found', status=status.HTTP_404_NOT_FOUND)

            response_data = {}
            response_data['message'] = "user found"

            s = mrloginSerializer(tt,many=False)
            


            return Response(s.data, status=status.HTTP_200_OK)

            # return HttpResponse(json.dumps(response_data), content_type="application/json")
            # return Response('user found', status=status.HTTP_201_CREATED)






class slideClassBassedView(APIView):

    def get(self, request, id=None ,format=None):
        if id is not None:
            
            try:
                tt = slide.objects.get(id=id)
            except:
                return Response('no data found', status=status.HTTP_404_NOT_FOUND)

            s = slideSerializer(tt,many=False)

            return Response(s.data, status=status.HTTP_200_OK)
        tt= slide.objects.all()
        s = slideSerializer(tt, many=True)
        return Response(s.data, status=status.HTTP_200_OK)




class testingClassBassedView(APIView):

    def get(self, request, id=None ,format=None):
        if id is not None:
            
            try:
                tt = testing.objects.get(id=id)
            except:
                return Response('no data found', status=status.HTTP_404_NOT_FOUND)

            s = testingSerializer(tt,many=False)

            return Response(s.data, status=status.HTTP_200_OK)
        tt= testing.objects.all()
        s = testingSerializer(tt, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request, id=None ,format=None):
        s = testingSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)

        return Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    
    def put(self, request, id=None ,format=None):
        try:
            tt=testing.objects.get(id=id)
        except:
            return Response("no data found ", status=status.HTTP_404_NOT_FOUND)
        s = testingSerializer(instance=tt, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    
    def delete(self, request, id=None ,format=None):
        try:
            tt= testing.objects.get(id=id)
        except:
            return Response("no data found ", status=status.HTTP_404_NOT_FOUND)
        tt.delete()
        return Response("deleted", status=status.HTTP_201_CREATED)




class pptClassBassedView(APIView):

    def get(self, request, category=None ,format=None, id=None):

        if id is not None:
            
            try:
                tt = ppt.objects.get(id=id)
            except:
                return Response('no data found', status=status.HTTP_404_NOT_FOUND)

            s = pptSerializer(tt,many=False)




            return Response(s.data, status=status.HTTP_200_OK)
        tt= ppt.objects.all()
        s = pptSerializer(tt, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request, id=None ,format=None,category=None):
        s = pptSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)

        return Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    
    def put(self, request, id=None ,format=None, category=None):
        try:
            tt=ppt.objects.get(id=id)
        except:
            return Response("no data found ", status=status.HTTP_404_NOT_FOUND)
        s = pptSerializer(instance=tt, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    
    def delete(self, request, id=None ,format=None, category=None):
        try:
            tt= ppt.objects.get(id=id)
        except:
            return Response("no data found ", status=status.HTTP_404_NOT_FOUND)
        tt.delete()
        return Response("deleted", status=status.HTTP_201_CREATED)






class ppt_filterClassBassedView(APIView):

    def get(self, request, category=None ,format=None):

        if category is not None:
            
            try:
                tt = ppt.objects.filter(category=category)
            except:
                return Response('no data found', status=status.HTTP_404_NOT_FOUND)

            s = pptSerializer(tt,many=True)


            return Response(s.data, status=status.HTTP_200_OK)
        # tt= ppt.objects.all()
        # s = pptSerializer(tt, many=True)
        # return Response(s.data, status=status.HTTP_200_OK)


class visit_mrClassBassedView(APIView):

    def get(self, request, mr_username=None ,format=None):

        if mr_username is not None:
            
            try:
                tt = visit.objects.filter(mr_username=mr_username)
            except:
                return Response('no data found', status=status.HTTP_404_NOT_FOUND)

            s = visit_mrSerializer(tt,many=True)


            return Response(s.data, status=status.HTTP_200_OK)
        # tt= ppt.objects.all()
        # s = pptSerializer(tt, many=True)
        # return Response(s.data, status=status.HTTP_200_OK)

