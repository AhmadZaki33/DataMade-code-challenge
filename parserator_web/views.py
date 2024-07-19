import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        address = request.query_params.get('address', None)
        if not address:
            return Response({
                'error': "Address parameter is required"
            }, status=400)

        try:
            address_components, address_type = self.parse(address)
            return Response({
                'address_components': address_components,
                'address_type': address_type
            })
        except usaddress.RepeatedLabelError:
            return Response({
                'error': "Cannot parse address with repeated labels"
            }, status=400)
        except Exception:
            return Response({
                'error': "Unable to parse the address"
            }, status=400)

    def parse(self, address):
        address_components, address_type = usaddress.tag(address)
        return address_components, address_type
