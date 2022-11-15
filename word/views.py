from rest_framework import viewsets
from word import serializers
from word.models import Word

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def word_detail(request, word):
    try:
        qr_word = Word.objects.get(word=word)
    except Word.DoesNotExist:
        return Response({"valid_word": False})

    # serializer_class = serializers.WordSerializer(wd)
    # serializer_class.data

    word_ac = qr_word.word_ac

    by_letter = {
    "l1": 0,
    "l2": 0,
    "l3": 0,
    "l4": 0,
    "l5": 0
    }

    return Response({"word": word, "word_ac": word_ac, "valid_word": True, "by_letter": by_letter})


# class WordViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     # http_method_names = ['get']
#     # serializer_class = serializers.WordSerializer
#     # queryset = models.Word.objects.all()

#     def get(self, request, format=None):
#         return Response({"message": "Hello, world!"})