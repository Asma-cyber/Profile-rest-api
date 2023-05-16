from rest_framework.views import APIView
from rest_framework.response  import Response 


class HelloApiView(APIView):
    """Test Api views """
    def get(self , request, format = None):
        """Return na list of apiview features """
        an_apiview= [
            'Uses HTTP methods as function (get, post, patch, put, delete)'
            'Is similar to a traditional Django view '
            'Gives you the most controle over your application logic '
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!','an_apiview': an_apiview})