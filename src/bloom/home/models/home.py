from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from cms.models.blocks import RawHTMLBlock
from wagtail.fields import RichTextField
from django import forms


class HomePage(Page):
    title_home = models.CharField(max_length=255,default='')
    body = StreamField([
        ('html', RawHTMLBlock()),
        ], blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel("body"),
        
    ]

    template = "home/home_page.html"
    



