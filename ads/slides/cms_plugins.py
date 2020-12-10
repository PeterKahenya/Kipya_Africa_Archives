from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import Slide,KipyaCard,CustomContent
from django.utils.translation import ugettext_lazy as _

@plugin_pool.register_plugin
class SlidePlugin(CMSPluginBase):
    model = Slide
    render_template = "slide.html"
    cache = False
    name=_("Slide")

@plugin_pool.register_plugin
class CardPlugin(CMSPluginBase):
    model = KipyaCard
    render_template = "card.html"
    cache = False
    name=_("Kipya Card")

@plugin_pool.register_plugin
class CustomPlugin(CMSPluginBase):
    model = CustomContent
    render_template = "custom.html"
    cache = False
    name=_("Custom Plugin")