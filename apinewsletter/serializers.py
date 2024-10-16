from rest_framework import serializers

from apinewsletter.models import  Article,Interest,Subscribe,SubscribeInterest

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = "__all__"



class InterestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Interest
        fields = "__all__"


class SubscribeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subscribe
        fields = "__all__"


class SubscribeInterestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SubscribeInterest
        fields = "__all__"
