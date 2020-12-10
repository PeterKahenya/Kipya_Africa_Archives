from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from .models import Iframe
from django.utils.translation import ugettext_lazy as _

@plugin_pool.register_plugin
class IFRAME(CMSPluginBase):
    model = Iframe
    render_template = "iframe.html"
    cache = False
    allow_children = True
    name=("IFRAME")

    def render(self, context, instance, placeholder):
        context = super(IFRAME, self).render(context, instance, placeholder)
        context.update({
            'objects_list': instance.child_plugin_instances,
        })
        return context