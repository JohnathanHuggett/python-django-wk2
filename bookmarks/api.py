from rest_framework import serializers, viewsets
from .models import BookMark, PersonalBookMark

# TODO -> CRITICAL -> disable this or change it so that only the admin can view


class BookMarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookMark
        fields = ('name', 'notes')


class BookMarkViewset(viewsets.ModelViewSet):
    serializer_class = BookMarkSerializer
    queryset = BookMark.objects.all()


class PersonalBookMarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookMark
        fields = ('name', 'notes')

    def create(self, validated_data):
        # import pdb
        # pdb.set_trace()
        user = self.context['request'].user
        personal_bookmark = PersonalBookMark.objects.create(
            user=user,
            **validated_data
        )
        return personal_bookmark


class PersonalBookMarkViewset(viewsets.ModelViewSet):
    serializer_class = PersonalBookMarkSerializer
    queryset = PersonalBookMark.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalBookMark.objects.none()

        else:
            return PersonalBookMark.objects.filter(user=user)
