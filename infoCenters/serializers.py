from rest_framework import serializers
from infoCenters.models import *

'''
    新闻
'''
class PassageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passage
        fields = "__all__"

    def create(self, validated_data):
        return Passage.objects.create(**validated_data)

'''
    美工图格
'''
class DMSerializer(serializers.ModelSerializer):
    class Meta:
        model = DMIMG
        fields = "__all__"

    def create(self, validated_data):
        return DMIMG.objects.create(**validated_data)

'''
    首页轮播图
'''
class VedioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vedio
        fields = "__all__"

    def create(self, validated_data):
        return Vedio.objects.create(**validated_data)

class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = "__all__"

    def create(self, validated_data):
        return Magazine.objects.create(**validated_data)

'''
    柱状图
'''
class BarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarModel
        fields = "__all__"

    def create(self, validated_data):
        return BarModel.objects.create(**validated_data)
'''
    折线图
'''
class LineModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineModel
        fields = "__all__"

    def create(self, validated_data):
        return LineModel.objects.create(**validated_data)

'''
    饼状图
'''
class PieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PieModel
        fields = "__all__"

    def create(self, validated_data):
        return PieModel.objects.create(**validated_data)

class MixModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MixModel
        fields = "__all__"

    def create(self, validated_data):
        return MixModel.objects.create(**validated_data)