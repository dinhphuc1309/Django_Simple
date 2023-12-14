from rest_framework import viewsets, permissions, filters

from django_filters.rest_framework import DjangoFilterBackend

from myapp.models import User

from myapp.serializers import UserSerializer

from myapp.permissions import IsUserOwner, IsSupperUser

from rest_framework.response import Response

from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSupperUser | IsUserOwner, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['is_superuser']
    search_fields = ['username', '=email']

    # def get_permissions(self):
    #     if self.action == 'retrieve':
    #         return [permissions.IsAuthenticated()]

    #     return [permissions.AllowAny()]

    @action(detail=False, methods=['get'])
    def extra_action_users(self, request):
        name = self.request.query_params.get('name', None)
        print(request.GET.get('name'))

        data = {'result': 'Extra action get list user'}

        if name is not None:
            data = {'result': f'Hello {name}'}

        return Response(data)
