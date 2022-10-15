from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from shsApp.serializers.citaSerializer import CitaSerializer

class CitaCreateView(views.APIView):

    permission_classes = [IsAuthenticated]
    
    def post (self, request, *args, **kwargs):

        data = {

            'especialidad':request.data.get('especialidad'),                     
            'user':request.data.get('user'),
            'medico':request.data.get('medico'),                     
            'fecha_cita':request.data.get('fecha_cita'),
            'hora_cita':request.data.get('hora_cita')                  
            
 

        }

        serializer = CitaSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

          