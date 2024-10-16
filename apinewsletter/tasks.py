# tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.template import Template, Context
from .models import Subscribe, Article

@shared_task
def send_newsletter_email(subscriber_id, article_id):
    subscriber = Subscribe.objects.get(id=subscriber_id)
    article = Article.objects.get(id=article_id)
    
    template = Template("""
    Bonjour {{ subscriber.user.first_name }},
    
    Nous pensons que cet article pourrait vous intéresser :
    
    {{ article.title }}
    
    {{ article.content|truncatewords:100 }}
    
    Lire plus : {{ article_url }}
    """)
    
    context = Context({
        'subscriber': subscriber,
        'article': article,
        'article_url': f"http://localhost:8000/articles/{article.id}/"
    })
    
    content = template.render(context)
    
    send_mail(
        subject=f"Nouvel article : {article.title}",
        message=content,
        from_email="newsletter@votre-site.com",
        recipient_list=[subscriber.email],
    )
    
    # EmailLog.objects.create(subscriber=subscriber, article=article)