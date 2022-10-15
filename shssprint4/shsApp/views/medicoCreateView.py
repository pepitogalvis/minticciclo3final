from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from shsApp.serializers.medicoSerializer import MedicoSerializer

class MedicoCreateView(views.APIView):

    permission_classes = [IsAuthenticated]
    
    def post (self, request, *args, **kwargs):

        data = {

            'name':request.data.get('name'),                     
            'last_name':request.data.get('last_name'),
            'phone':request.data.get('phone'),                     
            'especialidad_medico':request.data.get('especialidad_medico'),
            'tarjeta_profesional':request.data.get('tarjeta_profesional'),                     
            'documento_medico':request.data.get('documento_medico')
 

        }

        serializer = MedicoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
