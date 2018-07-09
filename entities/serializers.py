# -*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Entity
from entity_classes.serializers import EntityClassModelSerializer
from entity_types.serializers import EntityTypeModelSerializer
from entity_activities.serializers import EntityActivityModelSerializer



# Serializers define the API representation.
class EntityModelSerializer(serializers.ModelSerializer):
    entity_class = EntityClassModelSerializer()
    entity_type = EntityTypeModelSerializer()
    entity_activity = EntityActivityModelSerializer()
    class Meta:
        model = Entity
        fields = ['id', 'entity_class', 'entity_type', 'entity_activity', 'name', 'slogan', 'initials', 'logo', 'active', 'main']