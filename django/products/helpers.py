from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.forms.fields import ImageField as ImageFieldValidator
from rest_framework import serializers


class PartialViewSet(ModelViewSet):
    http_method_names = ["get", "post", "put", "patch", "options"]

    def put(self, requests):
        return Response(status=405)


def run_images_validators(images):
    if images == []:
        return

    if len(images) > 10:
        raise serializers.ValidationError(
            detail={
                "length": "Недопустимое кол-во файлов, максимальное кол-во файлов - 10"
            }
        )
