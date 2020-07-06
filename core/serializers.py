from core.models import List, Item
from rest_framework import serializers


class ItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = ['url', 'name', 'list', 'done']

class ListSerializer(serializers.HyperlinkedModelSerializer):

    item_set = ItemSerializer(many=True)

    class Meta:
        model = List
        fields = ['url', 'name', 'owner', 'item_set']