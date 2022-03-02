import faculty.models as models
import rest_framework.serializers as serializers


class FacultyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Faculty
        fields = ["id", "name", "title", "pic"]


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Faculty
        fields = '__all__'
