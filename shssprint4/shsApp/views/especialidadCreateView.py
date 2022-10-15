from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from shsApp.serializers.especialidadSerializer import EspecialidadSerializer

class EspecialidadCreateView(views.APIView):

    permission_classes = [IsAuthenticated]
    
    def post (self, request, *args, **kwargs):

        data = {

            'especialidad_id': request.data.get('especialidad_id'),
            'especialidad_nombre': request.data.get('especialidad_nombre')             
                    
        }       

        serializer = EspecialidadSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

       