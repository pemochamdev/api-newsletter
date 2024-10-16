from django.shortcuts import render

from apinewsletter.models import Article,Interest,Subscribe,SubscribeInterest
from apinewsletter.serializers import ArticleSerializer,InterestSerializer,SubscribeInterestSerializer,SubscribeSerializer

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class SubscribeViewset(viewsets.ModelViewSet):
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()
    
    @action(detail=True, methods=['post'])
    def subscribe(self, request, pk=None):
        subscribe = self.get_object()
        interests = request.data.get('interests', [])
        for interested_id in interests:
            
        
            SubscribeInterest.objects.create(subscribe=subscribe,interest_id=interested_id)
        return Response(
                {
                    'message':'subscribed to interest',
                },
                status=status.HTTP_201_CREATED)
        
    @action(detail=True, methods=['post'])
    def unsubscribe(self,request,pk=None):
        subscribe = self.get_object()
        interests = request.data.get('interests', [])
    
        SubscribeInterest.objects.filter(subscribe=subscribe,interest_id__in = interests).delete()
        return Response({'message':'unsubscribe successfully'},status=status.HTTP_202_ACCEPTED)


class InterestViewset(viewsets.ModelViewSet):
    serializer_class = InterestSerializer
    queryset = Interest.objects.all()



class ArticleViewset(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    
    
    @action(detail=True, methods=['post'])
    def send_newsletter(self, request, pk=None):
        article = self.get_object()
        subscribers = Subscribe.objects.filter(subscribeinterest__interest__in=article.tags.all()).distinct()
        for subscriber in subscribers:
            send_newsletter_email.delay(subscriber.id, article.id)
        return Response({'status': 'newsletter queued for sending'})
    